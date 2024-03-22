console.log("Hello Nicleonic")

let searchBt = document.getElementById('search');
let searchForm = document.getElementById('searchForm');

searchBt.addEventListener('click', (e)=>{
    if(searchForm.classList.contains('active')){
        searchForm.classList.remove('active')
    }
    else{
        searchForm.classList.add('active')
        document.getElementById('search-input').focus();
    }
})

document.getElementById('menu_btn').addEventListener("click", (e)=>{
    if( document.getElementById('menu_nav').classList.contains("active")){
        document.getElementById('menu_nav').classList.remove("active")
    }
    else{
        document.getElementById('menu_nav').classList.add('active')
    }
})

//---------------------------------------- Search Item ---------------------------
document.getElementById('search-input').addEventListener('input', function() {
    //var resultsContainer = document.getElementById('grid_section');
    //resultsContainer.innerHTML = "";
    var searchTerm = this.value;
    searchMedicament(searchTerm);
});

function searchMedicament(searchTerm) {
    var request = new XMLHttpRequest();
    request.open('GET', '/search-medicament/?q=' + searchTerm, true);
  
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var response = JSON.parse(request.responseText);
        updateResults(response);
      }
    };
  
    request.send();
}




//========================== updateResults =======================
function updateResults(results) {
    var resultsContainer = document.querySelector('.grid_section');
    resultsContainer.innerHTML = '';
    
    for (var i = 0; i < results.length; i++) {
      var medicament = results[i];
      var resultItem = document.createElement('a');
      //console.log(`Hey the item's id is ${parseInt(medicament.id)}`);
      console.log(`${medicament}`)
      console.log(JSON.stringify(medicament))
      resultItem.href = 'item/' + medicament.id;
      resultItem.innerHTML = `
        <div class="medocItem">
          <div class="imageItem">
            <img src="{% static "img/icon.png" %}" alt="">
          </div>
          <div class="details">
            <div class="title">
              ${medicament.nom}
            </div>
            <div class="count">
              Quantity : <span>${medicament.quantite}</span>
            </div>
            <div class="price">
              Price : <span><span>${medicament.prix}</span></span>Fc
            </div>
            <div class="dateExp">
              Exp. date : <span>${medicament.date_exp}</span>
            </div>
          </div>
        </div>
      `;
      resultsContainer.appendChild(resultItem);
    }
  }
//---------------------------------------------------


searchBt.addEventListener('click', (e)=>{
    if(searchForm.classList.contains('active')){
        searchForm.classList.remove('active')
    }
    else{
        searchForm.classList.add('active')
    }
})

document.getElementById('menu_btn').addEventListener("click", (e)=>{
    if( document.getElementById('menu_nav').classList.contains("active")){
        document.getElementById('menu_nav').classList.remove("active")
    }
    else{
        document.getElementById('menu_nav').classList.add('active')
    }
})
const anneeElement = document.getElementById('annee');
const anneeCourante = new Date().getFullYear();
anneeElement.textContent = anneeCourante;

