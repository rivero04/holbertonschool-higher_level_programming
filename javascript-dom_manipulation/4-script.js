document.getElementById('add_item').addEventListener('click', function() {
    let newLi = document.createElement('li');
    newLi.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newLi);
  });