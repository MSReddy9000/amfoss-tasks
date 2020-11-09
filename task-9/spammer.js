var msgSent = 0;
function spam()
{
    const x = 10
    document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = "Hi";
    $('.im_submit').trigger('mousedown');
    msgSent++
}
var spam = setInterval(spam, 1000);
function stopSpamming()
{
    clearInterval(spam);
}
if (msgSent > 10)
{
    stopSpamming;
}