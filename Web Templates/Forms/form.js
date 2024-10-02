function togglePassword(btn) {
  const input = btn.parentNode.querySelector('input');
  input.type = (input.type === 'password') ? 'text' : 'password';
}

const fechaInput = document.querySelector('input[type="date"]');

fechaInput.addEventListener('input', function() {
    if (this.value) {
        this.classList.add('has-date');
    } else {
        this.classList.remove('has-date');
    }
});

function showDatepicker(btn) {
  const input = btn.parentNode.querySelector('input');
  input.showPicker();
}
