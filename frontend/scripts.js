// Пример скрипта для модального окна
document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById('userModal');
  var closeModal = document.getElementsByClassName('close')[0];

  closeModal.onclick = function() {
      modal.style.display = 'none';
  }

  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = 'none';
      }
  }
});