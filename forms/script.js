$('nav a').click(function(e) {
  e.preventDefault();
  $('nav a').removeClass('active');
  $(this).addClass('active');
  if(this.id === !'store'){
    $('.store').addClass('noshow');
  }
  else if(this.id === 'store') {
    $('.store').removeClass('noshow');
    $('.rightbox').children().not('.store').addClass('noshow');
  }
  else if (this.id === 'profile') {
    $('.profile').removeClass('noshow');
     $('.rightbox').children().not('.profile').addClass('noshow');
  }
});
document.getElementById("submit").addEventListener("click", send_form);

function send_form() {
  var user = get_data();
  console.log(user);
  var url = 'http://54.157.184.202/api/users';
  fetch(url, {
    method: 'POST', 
    body: JSON.stringify(user),
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
  .catch(error => console.error('Error:', 'No se puede crear un usario con los datos suministrados'))
  .then(response => console.log('Success:', response));
  clean_form();
};

function get_data() {
  var user_info = {};
  user_info.name = document.getElementById("fname").value;
  user_info.email = document.getElementById("email").value;
  user_info.passwd = document.getElementById("password").value;
  user_info.type = "client";
  user_info.mobile = document.getElementById("phone").value;
  return user_info;
};

function clean_form(){
  document.getElementById("fname").value = "";
  document.getElementById("email").value = "";
  document.getElementById("password").value = "";
  document.getElementById("phone").value = "";

};

