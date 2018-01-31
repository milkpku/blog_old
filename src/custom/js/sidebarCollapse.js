function openSidebar() {
  document.getElementById("sidebar").style.width = "200px";
  $("#overlay").fadeIn();
};

function closeSidebar() {
  document.getElementById("sidebar").style.width = "0";
  $("#overlay").fadeOut();
};

$(document).ready(function(){
  $("#sidebarCollapse").on('click', openSidebar);
  $("#sidebarDismiss, #overlay").on('click', closeSidebar);
});