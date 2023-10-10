# Environments and Languages 

## Development Environments

- Windows 10 Education
- [GitBash 2.42.0 64-bit](https://git-scm.com/download/win) -> Type in these commands in GitBash to clone down the files onto your computer:
```
git clone https://github.com/NTIG-Uppsala/Cafeteria-skylt.git
```
- Visual Studio Code - (Version 1.83.0)
- Google Chrome - (Version 117.0.5938.134)
- Microsoft Edge - (Version 117.0.2045.60)

***

## Programming Languages & Frameworks

### Programming Languages:
- JavaScript
- HTML5
- CSS3
- Python3 (for testing)

### Frameworks: (Compiled CSS and JS)
- [jQuery 3.3.1](https://jquery.com/download/)
- [Bootstrap 5.3.2.](https://getbootstrap.com/docs/4.3/getting-started/download/) 
- [chromedriver 114.0.5735.90](https://chromedriver.chromium.org/downloads) (for testing)
- [Java 8 update 381](https://www.java.com/sv/download/) (for testing)	

### Plugins:
For testing
```
Selenium 4.13.0				
pip install selenium==4.13.0

Unittest
```

***

## Coding Standard 

- Standard for indents is one indent 
	```
    <html>

	    <body> 
		    <div>
	            </div>
	    </body>
	    
	</html>
    ```
- camelCase
- The standard language for variable names, class names and such is english.
- Comments in html are written this way: \<!-- This is a comment -->
- Comments in css are written this way: /* This is a comment */
- Comments in Python are written with hashtags at the beginning of the line and starts with a blankspace and an uppercase letter: # This is a comment
- HTML5 Style Guide is to be followed -> [W3Schools HTML5 Style Guide](https://www.w3schools.com/html/html5_syntax.asp)
- Variables should match in indentation -> if (var1, var2, var3, var4)

***

## Tips

### How to add a slide:

```html
<div class="carousel-item slide" data-interval="10000" style= "background-color: #190f27;">
	<img src="images/small-toast.png" alt="..." class="productslide " id="toast" >
	<img src="images/dot.png" alt="..." class="productslide" id="dot">
	<img src="images/money-dot.png" alt="..." class="productslide" id="moneydot">
	<div class="carousel-caption d-none d-md-block" id="productprice">
		<p class="toast-text">Toast</p>
		<p class="price">20 kr</p>
	</div>

</div>
```

The first div-tag tells you that this is a slide (class="carousel-item slide''), everything within this tag is a part of the slide.

To create a new slide, copy the code above and put it under the existing "carousel-item" tags <br>
Note: Images should have a width between 950-1000px and a height of 600-700px.

### data-interval
```
data-interval="10000" determines how many milliseconds have to pass before it changes to the next slide, 10000ms is 10 seconds
```

### id
 
 ```
id="ImageName" is only used to position images.
The id for dot.png and money-dot.png is recommended to be used for all slides as they position the purple bubbles with the price on.
Id:s that are used to position a product can be created and adjusted but make sure that the whole image is within the bubble.
Make sure that the product's id has "z-index: 1;" so that it is on the correct layer. 

id="pricetoast" is used to position the text and to put the text on the top layer.
This should not be changed although depending on the length of the text a new id may be necessary.
Make sure that the price is always in the bubble.
```



