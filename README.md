# Instruktioner för användning

Development (inte klara features) pushas till development branch

### Hur du lägger in en slide:

```html
<div class="carousel-item slide" data-interval="10000" style= "background-color: #190f27;">
	<img src="images/small-toast.png" alt="..." class="productslide " id="toast" >
	<img src="images/dot.png" alt="..." class="productslide" id="dot">
	<img src="images/money-dot.png" alt="..." class="productslide" id="moneydot">
	<div class="carousel-caption d-none d-md-block" id="productprice">
		<p class="toast-text">Toast</p>
		<p class="price">15 kr</p>
	</div>

</div>
```

Den första div-taggen säger detta är en slide (se class="carousel-item slide), allt som ligger i denna div-tagg är en del av sliden.

För att skapa en ny slide kan du kopiera denna kod och lägga den under de redan existerande "carousel-item" div taggarna.
Lägg den nya bilden till sliden i image mappen. Ändra sedan den första "img" taggens source till "images/namnetpåbilden.png".
Note: Bilder borde vara mellan 950-1000px breda och 600-700px höga.
Det du kommer behöva göra är att ett nytt id för den nya bilden:

```css
#korv{
    z-index:1;
    bottom:675px;
    left: 50px;
}
```

Kopiera denna kod och lägg längst ner i prislistacss dokumentet. Döp om den från korv till ett mer passande namn.
I samma rad som du ändrade "img" taggen behöver du nu ändra id till det nya id namnet du skapade.
"bottom" innebär hur många pixlar från botten bilden är och "left" hur långt från vänster.
Ändra dessa värden för att positionera bilden.

I "p" taggarna ska du byta ut namnet och priset.

### En förklaring och användingen av alla klasser samt JavaScript;

***


#### div-tagg för slide

##### data-interval

    data-interval="10000" är hur långt tid det tar innan sliden byts till nästa.
    Denna tid mäts i ms (millisekunder)där 10000ms är ekvalent med 10 sekunder. 
    För att förändra antalet sekunder en slide visas ändra data-interval="" till önskad tid i millisekunder.


##### style

    style="background-color: #190f27" är endast för den mörklila bakgrundsfärgen och bör inte ändras.
    Alla slides rekommenderas att använda samma färg för sammanhållningens skull. 
    Om denna ändras se till att ändra alla andra slides till samma eller snarlika färger.

***



#### img-tagg


##### src

    src="images/small-toast.png" detta säger vilken bild på varan som kommer att visas på en slide.
    För att lägga till ny bild för en  slide; spara den i .png format, namnge den till ett passande namn och lägg den sedan i images mappen. 


##### class

    class="toastslide" används för att se til att alla objekt på sliden har "position: absolute;".
    Detta för att deras position inte ska påverkas av varandra eller andra statiska objekt.
    Det är rekommenderat att varje slide får en egen klass som gör samma sak; dvs endast sätter position: absolute; på sliden. 


##### alt

    alt="..." används huvudsakligen för att beskriva en bild när den inte laddats in korrekt på en hemsida. Taggen ska finnas på alla <img>-taggar, den ska inte ändras. 

##### id

    id="NamnPåImageFilen" används endas för att positionera bilderna. Från Exempelkoden Toast syns det att varje <img>- tagg har ett unikt id, detta bestämmer positionen på det objektet.
    Id för dot.png samt money-dot.png rekommenderas att användas för alla slides, dessa två positionerar de lila bubblorna som bilden på varan och priser ligger i.
    Små förändringar på dessa får ej göras. Dessa ska vara samma på alla slides.
    Id som används för att positionera en vara (se id="toast") får skapas och justeras men se till att hela bilden ligger i bubblan, detta måste göras manuellt.
    Se till att varans id innehåller "z-index: 1;" för att lägga varan på rätt lager. 


***




#### div-tagg för text i slide

##### class

    class="carousel-caption d-none d-md-block" används för att lägga in text, all text som ska finnas på sliden (se <p>-tagg).
    Varje text del ska ligga i en egen <p>-tagg i <div class="carousel-caption d-none d-md-block">-taggen. 
    

##### id


    id="pricetoast" används för att positionera texten och för att lägga texten på det översta lagret.
    Denna bör inte ändras men beroende på länged på varans namn (se <p class="toast-text">) så kan ett nytt id behövas att skapas manuellt med ett relevant namn.
    Se till att priset (se <p class="price">) alltid ligger i bubblan.
    

***




#### p-tagg för text

##### class


    class="toast-text" samt class="price" säger vilken font-size texten ska ha.
    Denna storlek på texten ska användas på alla varunamn respektive priser. Den får inte ändras.
    


***













