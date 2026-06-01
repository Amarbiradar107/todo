const baseUrl = 'http://127.0.0.1:8000/';

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('login-btn');
  if (!btn) return;

  btn.addEventListener('click', async (e) => {
    e.preventDefault();

    const emailInput = document.querySelector('.auth-form-box .form-stack input[type="email"]') || document.querySelector('input[type="email"]');
    const passwordInput = document.getElementById('pwd') || document.querySelector('.auth-form-box input[type="password"]');
    const usernameOrEmail = (emailInput && emailInput.value) ? emailInput.value.trim() : '';
    const password = passwordInput ? passwordInput.value : '';

    if (!usernameOrEmail || !password) {
      alert('Please enter both email/username and password.');
      return;
    }

    try {
      const resp = await fetch(`${baseUrl}users/api/token/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: usernameOrEmail, password })
      });

      const data = await resp.json().catch(() => ({}));
      if (resp.ok) {
        // Save tokens
        if (data.access) localStorage.setItem('access_token', data.access);
        if (data.refresh) localStorage.setItem('refresh_token', data.refresh);
        alert('Login successful');
        // Redirect to dashboard (same folder)
        window.location.href = 'dashboard.html';
      } else {
        const msg = data.detail || data.non_field_errors || JSON.stringify(data);
        alert('Login failed: ' + msg);
        console.error('Login error:', data);
      }
    } catch (err) {
      console.error('Network/login error:', err);
      alert('Network error. See console for details.');
    }
  });
});
