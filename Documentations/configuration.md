
# Tips

## How to add a slide:

```html
	<div class="carousel-item slide" data-interval="5000" style="background-color: #190f27;">
		<img src="images/toast2NoBoard.png" alt="..." class="productSlide productImage">
		<img src="images/dot.png" alt="..." class="productSlide dot">
		<img src="images/money-dot.png" alt="..." class="productSlide moneyDot">
		<div class="carousel-caption d-none d-md-block productPrice">
			<p class="itemText">Toast</p>
			<p class="price">20 kr</p>
		</div>

	</div>
```

The first div-tag tells you that this is a slide (class="carousel-item slide''), everything within this tag is a part of the slide.

To create a new slide, copy the code above and put it under the existing "carousel-item" tags <br>
Note: Images should have a width between 950-1000px and a height of 600-700px.

## data-interval
```
data-interval="10000" determines how many milliseconds have to pass before it changes to the next slide, 10000ms is 10 seconds
```

## id
 
 ```
id="ImageName" is only used to position images.
The id for dot.png and money-dot.png is recommended to be used for all slides as they position the purple bubbles with the price on.
Id:s that are used to position a product can be created and adjusted but make sure that the whole image is within the bubble.
Make sure that the product's id has "z-index: 1;" so that it is on the correct layer. 

id="priceToast" is used to position the text and to put the text on the top layer.
This should not be changed although depending on the length of the text a new id may be necessary.
Make sure that the price is always in the bubble.
```



