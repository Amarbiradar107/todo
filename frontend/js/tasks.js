const baseUrl = 'http://127.0.0.1:8000/';

function getAuthHeaders() {
  const headers = { 'Content-Type': 'application/json' };
  const token = localStorage.getItem('access_token');
  if (token) headers['Authorization'] = 'Bearer ' + token;
  return headers;
}

async function fetchTasks() {
  const tbody = document.getElementById('tasks-tbody');
  if (!tbody) return;
  try {
    const res = await fetch(`${baseUrl}tasks/task-list/`, { headers: getAuthHeaders() });
    if (res.status === 401) {
      alert('Not authenticated. Please login.');
      window.location.href = 'login.html';
      return;
    }
    const data = await res.json();
    renderTasks(data);
  } catch (err) {
    console.error('Error fetching tasks', err);
    tbody.innerHTML = '<tr><td colspan="6">Failed to load tasks.</td></tr>';
  }
}

function renderTasks(tasks) {
  const tbody = document.getElementById('tasks-tbody');
  if (!tbody) return;
  if (!Array.isArray(tasks) || tasks.length === 0) {
    tbody.innerHTML = '<tr><td colspan="6">No tasks found.</td></tr>';
    return;
  }

  tbody.innerHTML = tasks.map(task => {
    const due = task.due_date || '';
    const priority = (task.priority || '').toLowerCase();
    const status = (task.status || '').toLowerCase();
    const priorityBadge = `<span class="badge badge-${priority}">${priority.charAt(0).toUpperCase() + priority.slice(1)}</span>`;
    const statusText = status === 'completed' ? `<span style="color: var(--success); font-weight: 600;">Completed</span>` : (status === 'in_progress' ? `<span style="color: var(--primary); font-weight: 600;">In Progress</span>` : `<span style="color: var(--warning); font-weight: 600;">Pending</span>`);
    return `
      <tr>
        <td><strong>${escapeHtml(task.title || '')}</strong></td>
        <td>—</td>
        <td>${priorityBadge}</td>
        <td>${due}</td>
        <td>${statusText}</td>
        <td>
          <a href="edit-task.html?id=${task.task_id}" style="text-decoration: none; margin-right: 12px;">✏️</a>
          <a href="#" data-id="${task.task_id}" class="delete-link" style="text-decoration: none;">🗑️</a>
        </td>
      </tr>`;
  }).join('');

  // attach delete handlers
  document.querySelectorAll('.delete-link').forEach(a => {
    a.addEventListener('click', async (e) => {
      e.preventDefault();
      const id = a.getAttribute('data-id');
      if (!confirm('Delete this task?')) return;
      try {
        const res = await fetch(`${baseUrl}tasks/task-delete/${id}/`, { method: 'DELETE', headers: getAuthHeaders() });
        if (res.ok) {
          fetchTasks();
        } else {
          const d = await res.json().catch(()=>({}));
          alert('Delete failed: ' + (d.detail || JSON.stringify(d)));
        }
      } catch (err) {
        console.error('Delete error', err);
        alert('Network error deleting task');
      }
    });
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&"'<>]/g, function (m) { return ({'&':'&amp;','"':'&quot;','\'':'&#39;','<':'&lt;','>':'&gt;'})[m]; });
}

// Create task
const createForm = document.getElementById('create-task-form');
if (createForm) {
  document.getElementById('create-task-btn').addEventListener('click', async (e) => {
    const title = createForm.querySelector('input[type="text"]').value.trim();
    const description = createForm.querySelector('textarea').value.trim();
    const priority = createForm.querySelector('select:nth-of-type(2)').value.toLowerCase();
    const dueDate = createForm.querySelector('input[type="date"]').value;

    if (!title) { alert('Title is required'); return; }

    try {
      const res = await fetch(`${baseUrl}tasks/task-list/`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: JSON.stringify({ title, description, priority, status: 'pending', due_date: dueDate })
      });
      if (res.ok) {
        alert('Task created');
        window.location.href = 'tasks.html';
      } else {
        const d = await res.json().catch(()=>({}));
        alert('Create failed: ' + (d.detail || JSON.stringify(d)));
      }
    } catch (err) {
      console.error('Create task error', err);
      alert('Network error creating task');
    }
  });
}

// Edit task page
const editForm = document.getElementById('edit-task-form');
if (editForm) {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');
  if (!id) {
    alert('No task id provided');
  } else {
    // populate
    (async () => {
      try {
        const res = await fetch(`${baseUrl}tasks/task-detail/${id}/`, { headers: getAuthHeaders() });
        if (res.ok) {
          const task = await res.json();
          editForm.querySelector('input[type="text"]').value = task.title || '';
          editForm.querySelector('textarea').value = task.description || '';
          const selects = editForm.querySelectorAll('select');
          if (selects[0]) selects[0].value = task.category || selects[0].value;
          if (selects[1]) selects[1].value = task.priority || selects[1].value;
          editForm.querySelector('input[type="date"]').value = task.due_date || '';
        } else {
          const d = await res.json().catch(()=>({}));
          alert('Failed to load task: ' + (d.detail || JSON.stringify(d)));
        }
      } catch (err) {
        console.error('Load task error', err);
        alert('Network error loading task');
      }
    })();

    // update
    document.getElementById('update-task-btn').addEventListener('click', async () => {
      const title = editForm.querySelector('input[type="text"]').value.trim();
      const description = editForm.querySelector('textarea').value.trim();
      const priority = editForm.querySelector('select:nth-of-type(2)').value.toLowerCase();
      const dueDate = editForm.querySelector('input[type="date"]').value;
      try {
        const res = await fetch(`${baseUrl}tasks/task-detail/${id}/`, {
          method: 'PUT',
          headers: getAuthHeaders(),
          body: JSON.stringify({ title, description, priority, status: 'pending', due_date: dueDate })
        });
        if (res.ok) {
          alert('Task updated');
          window.location.href = 'tasks.html';
        } else {
          const d = await res.json().catch(()=>({}));
          alert('Update failed: ' + (d.detail || JSON.stringify(d)));
        }
      } catch (err) {
        console.error('Update error', err);
        alert('Network error updating task');
      }
    });

    // delete
    const delBtn = document.getElementById('delete-task-btn');
    if (delBtn) {
      delBtn.addEventListener('click', async () => {
        if (!confirm('Delete this task?')) return;
        try {
          const res = await fetch(`${baseUrl}tasks/task-delete/${id}/`, { method: 'DELETE', headers: getAuthHeaders() });
          if (res.ok) {
            alert('Task deleted');
            window.location.href = 'tasks.html';
          } else {
            const d = await res.json().catch(()=>({}));
            alert('Delete failed: ' + (d.detail || JSON.stringify(d)));
          }
        } catch (err) {
          console.error('Delete error', err);
          alert('Network error deleting task');
        }
      });
    }
  }
}

// auto-run fetch on tasks page
if (document.getElementById('tasks-tbody')) fetchTasks();
