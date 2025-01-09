document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById('userModal');
  var modalImage = document.getElementById('modalImage');
  var modalName = document.getElementById('modalName');
  var modalEmail = document.getElementById('modalEmail');
  var modalBirth = document.getElementById('modalBirth');
  var modalCity = document.getElementById('modalCity');
  var span = document.getElementsByClassName('close')[0];

  document.querySelectorAll('.user-card').forEach(card => {
      card.addEventListener('click', function() {
          modal.style.display = 'block';
          modalImage.src = this.querySelector('img').src;
          modalName.textContent = this.getAttribute('data-name');
          modalEmail.textContent = 'Email: ' + this.getAttribute('data-email');
          modalBirth.textContent = 'Дата рождения: ' + this.getAttribute('data-birth');
          modalCity.textContent = 'Город: ' + this.getAttribute('data-city');
      });
  });

  span.onclick = function() {
      modal.style.display = 'none';
  }

  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = 'none';
      }
  }
});