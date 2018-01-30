function openSidebar() {
  document.getElementById("sidebar").style.width = "250px";
  $("#overlay").fadeIn();
};

function closeSidebar() {
  document.getElementById("sidebar").style.width = "0";
  $("#overlay").fadeOut();
};

$(document).ready(function(){
  $("#sidebarCollapse").on('click', openSidebar);
  $("#sidebarDismiss").on('click', closeSidebar);
});