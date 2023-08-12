copyText = () => {
  //get the text to copy
  var textToCopy = document.querySelector("#result");
  //focus on and then select the text to copy
  textToCopy.focus();
  textToCopy.select();

  //copy the text
  document.execCommand("copy");
  //Show the "check" notification
  let checkMark = document.querySelector(".CopyNotification");
  checkMark.classList.remove("hidden");
};
//Get the copy button
var copyButton = document.querySelector(".copyButton");
copyButton.addEventListener("click", copyText);
