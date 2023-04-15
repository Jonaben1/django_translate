
const textArea = document.getElementById('translate');
textArea.addEventListener('input', () => {
    var textLn =  textArea.value;
    document.getElementById('countText').innerHTML='Total words: '+getCount(textLn);
});


const lan = document.getElementById('text');
lan.addEventListener('input', () => {
    let textLen =  lan.value;
    document.getElementById('wordCount').innerHTML='Total words: '+getCount(textLen);
});

getCount = str => {
 return str.split(' ').filter(num => {
  return num != ''
 }).length;
}
