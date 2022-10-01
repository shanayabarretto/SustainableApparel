console.log( "This is my extension");

let paragraphs = document.getElementsByTagName('p')
for (elt of paragraphs)
{
    elt.style['background-color'] = '#FF10FF';
}