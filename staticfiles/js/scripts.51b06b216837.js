document.addEventListener("DOMContentLoaded", function () {
  console.log("Welcome to ForfreeLetters!");

  // Update the year in the footer
  var currentYear = new Date().getFullYear();
  document.getElementById("footerCurrentYear").textContent = currentYear;

  const navIcon = document.getElementById("toggleNav");
  const navIcon2 = document.getElementById("toggleNav2");

  const mobile__nav = document.getElementById("mobile__nav");

  navIcon.addEventListener("click", function () {
    mobile__nav.classList.toggle("hide");
  });

  navIcon2.addEventListener("click", function () {
    mobile__nav.classList.toggle("hide");
  });
});
