function enableInput () {
  $('input, select').removeAttr('disabled');
  return false;
}

function disableInput () {
  $('input, select').attr('disabled', 'disabled');
  return false;
}
