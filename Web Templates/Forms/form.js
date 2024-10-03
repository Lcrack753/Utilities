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
function showFileinput(btn) {
  const input = btn.querySelector('input');
  input.click()
}
function fileInputChange(fileInput) {
  const fileInputContainer = fileInput.parentNode
  if (fileInput.files.length > 0) {
    fileInputContainer.classList.add("file-selected");
  } else {
    fileInputContainer.classList.remove("file-selected");
  }
}
