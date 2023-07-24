// Get Modal to display product image
var modal = document.getElementById("imgView{{product.id}}");

// Alt text is product name, used as caption for image
var img = document.getElementById("product{{product.id}}");

var modalImg = document.getElementById("product{{product.id}}");
var captionText = document.getElementById("caption");

img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

// Retrieve close element
var span = document.getElementsByClassName("close")[0];

// Onclick X, closes the modal
span.onclick = function() {
    modal.style.display = "none";
}