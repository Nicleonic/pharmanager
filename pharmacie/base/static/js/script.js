    //============================= Tooltip
    function createTooltip(element, tooltipText) {
      var tooltip = document.createElement('div');
      //tooltip.classList.add('tooltip_class');
      tooltip.className = 'tooltip';
      tooltip.textContent = tooltipText;
      
      element.addEventListener('mouseover', function() {
        tooltip.style.display = 'block';
      });
    
      element.addEventListener('mouseout', function() {
        tooltip.style.display = 'none';
      });
    
      element.appendChild(tooltip);
  }
  //---------------------------------------------------------
  // var button = document.getElementById('myButton');
  // createTooltip(button, 'Texte du tooltip');

  createTooltip(document.getElementById("med_delete"), "Supprimer l'element")
  createTooltip(document.getElementById("med_edit"), "Modifier l'element")

  //---------------------------------------------