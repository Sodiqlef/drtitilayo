  function whatsapp() {
      var first = document.getElementById("first").value;
      var last = document.getElementById("last").value;
      var email = document.getElementById("email").value;
      var phone = document.getElementById("phone").value;
      var message = document.getElementById("message").value;

      var url = "https://wa.me/2349024057678?text=" +
          "*Name :* " + first + ' ' + last + "%0a" +
          "*Email :* " + email + "%0a" +
          "*Phone :* " + phone + "%0a" +
          "*Message :* " + message;

      window.open(url, '_blank').focus();
  }