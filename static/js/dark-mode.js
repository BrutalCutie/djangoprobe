document.getElementById('darkmode').onclick = darkMode;



function darkMode() {
  var element = document.body;
  element.classList.toggle("dark-mode");
}