/**
 * Created by summerlynbryant on 8/28/15.
 */
    //this takes the stored 'name' from validate.js and adds it to the
    // gallery greeting
var el = document.querySelector(".tagline");
console.log(el);
var welcome = el.textContent;
var galleryGreeting = "develop something beautiful, ";
var name = sessionStorage.getItem("name");
el.textContent = galleryGreeting + name;


var gallery = document.getElementById('gallery');
//this function generates the gallery . I used an open source lightbox to
// generate the clickable images to pull up a single larger image
var generateGallery = function () {
	var galleryHTML = '<ul>';

	for (i = 1; i <= 60; i++) {

		if (i < 10) {
			i = "0" + i;
		}
		// concatonating  image within the li that starts and ends with same
		// format. I included the open source lightbox data as well.
		galleryHTML += '<li>';
		galleryHTML += '<a href="images/pdxcg_';
		galleryHTML += i + '.jpg" data-lightbox="gallery">';
		galleryHTML += '<img src="images/pdxcg_';
		galleryHTML += i + '.jpg">';
		galleryHTML += '</a></li>';
	}

	galleryHTML += '</ul>';
	gallery.innerHTML = galleryHTML;
};
// called the function to generate the pretty gallery
generateGallery();