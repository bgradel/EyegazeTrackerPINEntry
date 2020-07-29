class PinLogin {

    

    constructor ({el, pageinfo, redirectTo, maxNumbers = Infinity}) {
        this.el = {
            main: el,
            numPad: el.querySelector(".pin-login__numpad"),
            textDisplay: el.querySelector(".pin-login__text")
        };

         

        this.pageinfo = pageinfo;
        this.redirectTo = redirectTo;
        this.maxNumbers = maxNumbers;
        this.value = "";
        
        
        if (pageinfo == "first"){
            this._generatePad1()
        }else if (pageinfo == "second"){
            this._generatePad2()
        }else if (pageinfo == "third"){
            this._generatePad3()
        }
        
    }

    _generatePad1() {
        const padLayout = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            ,"00","0"
        ];

        padLayout.forEach(key => {
            const insertBreak = key.search(/[369]/) !== -1;
            const keyEl = document.createElement("div");

            keyEl.classList.add("pin-login__key");
            keyEl.classList.toggle("material-icons", isNaN(key));
            keyEl.textContent = key;
            keyEl.addEventListener("click", () => { this._handleKeyPress(key) });
            this.el.numPad.appendChild(keyEl);
            if (keyEl.textContent == "00"){
                this.el.numPad.appendChild(keyEl)
                keyEl.style.visibility = "hidden"
            }
            if (insertBreak) {
                this.el.numPad.appendChild(document.createElement("br"));
            }
        });

        console.log(screen.width,screen.height)
        this._createDiv();
    }

    _generatePad2(){
        const padLayout = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            ,"0"
        ];

        padLayout.forEach(key => {
            const insertBreak = key.search(/[5]/) !== -1;
            const keyEl = document.createElement("div");

            keyEl.classList.add("pin-login__key");
            keyEl.classList.toggle("material-icons", isNaN(key));
            keyEl.textContent = key;
            keyEl.addEventListener("click", () => { this._handleKeyPress(key) });
            this.el.numPad.appendChild(keyEl);

            if (insertBreak) {
                this.el.numPad.appendChild(document.createElement("br"));
            }
        });

    }

    _generatePad3(){
        const padLayout = [
            "0","1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            
        ];
        const sw = Number(screen.width)/2
        const sh = Number(screen.height)/2
        const buttonSize = 150
        const coord = [["853px","853px"],["629px","982px"],["371px","982px"],["147px","853px"],["18px","371px"],["18px","629px"],["147px","147px"],["371px","18px"],["629px","18px"],["853px","147px"]]
        const coord_testing = [["1034px","557px"],["698px","637px"],["362px","637px"],["27px","562px"],["-230px","400px"],["-403px","237px"],["-490px","77px"],["-500px","0px"],["-510px","0px"],["-523px","77px"]]
        const coordf = [[(sw + buttonSize + buttonSize/2).toString(),(sh + buttonSize + buttonSize/2).toString()],
        [(sw + buttonSize/2).toString(),(sh + buttonSize + buttonSize).toString()],
        [(sw - buttonSize/2).toString(),(sh + buttonSize + buttonSize).toString()],
        [(sw - buttonSize - buttonSize/2).toString(),(sh + buttonSize + buttonSize/2).toString()],
        [(sw - buttonSize*2).toString(),(sh + buttonSize/2).toString()],
        [(sw - buttonSize*2).toString(),(sh - buttonSize/2).toString()],
        [(sw - buttonSize - buttonSize/2).toString(),(sh - buttonSize - buttonSize/2).toString()],
        [(sw + buttonSize/2).toString(),(sh - buttonSize*2).toString()],
        [(sw - buttonSize/2).toString(),(sh - buttonSize*2).toString()],
        [(sw + buttonSize + buttonSize/2).toString(),(sh - buttonSize - buttonSize/2).toString()]]
        var i = 0;
        padLayout.forEach(key => {
            
            
            console.log(i);
            console.log(coord[i][1]);
            const keyEl = document.createElement("div");

            keyEl.classList.add("pin-login__key");
            keyEl.classList.toggle("material-icons", isNaN(key));
            keyEl.textContent = key;
            keyEl.addEventListener("click", () => { this._handleKeyPress(key) });
            this.el.numPad.appendChild(keyEl);
            keyEl.style.cssText = "position:absolute; border:1px solid blue;";
            var va = getPos(keyEl);
            keyEl.style.left = (Number(coordf[i][0])-90).toString().concat("px");
            keyEl.style.top =  (Number(coordf[i][1])-20).toString().concat("px");
           
            console.log((Number(coordf[i][0])-90).toString().concat("psx"));
            console.log((Number(coordf[i][1])).toString().concat("psx"));
            var va = getPos(keyEl);
            console.log(((va.x).toString().concat("pssx")));
            console.log(((va.y).toString().concat("pssx")));
            //console.log(x,y);
            i = i + 1;
        });

    }

    _createDiv(){
        
        var buttons = document.createElement("button");
        buttons.textContent = "Delete"
        buttons.style.fontSize = "20px";
        buttons.style.height = "60px";
        buttons.style.width = "90px";
        //this.el.numPad.appendChild(button);
        this.el.numPad.appendChild(buttons);
        buttons.addEventListener("click", () => { this._handleKeyPress(buttons.textContent) });

        const sw = Number(screen.width)/2
        const sh = Number(screen.height)/2
        
        this.password = this._randPass();
        // create a new div element 
        var newDiv = document.createElement("div"); 
        // and give it some content 
        var newDiv1 = document.createElement("div");
        var newContent = document.createTextNode("your new password is: "); 
        newDiv1.style.width = "400px";
        newDiv1.style.height = "40px";
        newDiv1.style.marginTop = "20px";
        newDiv1.style.textAlign = "center";

        var newDiv2 = document.createElement("div");
        var newPassword = document.createTextNode(this.password.toString()); 
        newDiv2.style.width = "400px";
        newDiv2.style.height = "40px";
        newDiv2.style.fontSize = "40px";
        newDiv2.style.textAlign = "center";

        var newDiv3 = document.createElement("div");
        var newContent2 = document.createTextNode("press ok when ready to enter the password"); 
        newDiv3.style.width = "400px";
        newDiv3.style.height = "40px";
        newDiv3.style.marginTop = "30px";
        newDiv3.style.textAlign = "center";
        

        newDiv.style.cssText = "position:absolute; border:1px solid blue";
        newDiv.style.height = "200px";
        newDiv.style.width = "400px";
        newDiv.style.background = "white";
        newDiv.style.textAlign = "center";

        newDiv.appendChild(newDiv1);
        newDiv.appendChild(newDiv2);
        newDiv.appendChild(newDiv3);
        // add the text node to the newly created div
        newDiv1.appendChild(newContent);  
        newDiv2.appendChild(newPassword);
        newDiv3.appendChild(newContent2);
        newDiv.style.top = (sh-100).toString().concat("px");
        newDiv.style.left = (sw-200).toString().concat("px");
        
        var button = document.createElement("button");
        button.innerHTML = "ok";

        newDiv.appendChild(button);

        // 3. Add event handler
        button.addEventListener ("click", function() {
            newDiv.style = "display:none";
        });
        
        // add the newly created element and its content into the DOM 
        var currentDiv = document.getElementById("div1"); 
        document.body.insertBefore(newDiv, currentDiv); 
    }

    _createDiv2(){
        
        const sw = Number(screen.width)/2
        const sh = Number(screen.height)/2

        this.password = this._randPass();
        // create a new div element 
        var newDiv = document.createElement("div"); 
        // and give it some content 
        var newContent = document.createTextNode("press continu to go to next page"); 
        newDiv.style.cssText = "position:absolute; border:1px solid blue";
        newDiv.style.height = "200px";
        newDiv.style.width = "400px";
        newDiv.style.background = "white";
        // add the text node to the newly created div
        newDiv.appendChild(newContent);  
        newDiv.style.top = "500px";
        newDiv.style.left = "900px";
        
        var button = document.createElement("button");
        button.innerHTML = "ok";

        newDiv.appendChild(button);

        // 3. Add event handler
        button.addEventListener ("click", function() {
            newDiv.style = "display:none";
        });
        
        // add the newly created element and its content into the DOM 
        var currentDiv = document.getElementById("div1"); 
        document.body.insertBefore(newDiv, currentDiv); 
    }


    _handleKeyPress(key){
        if (key == "Delete"){
            console.log(key);
            this.value = this.value.substring(0, this.value.length - 1);
            this._updateValueText();
        }
        console.log(key)
        if (this.value.length < this.maxNumbers && !isNaN(key)){
            this.value += key;
        }
        console.log(this.value)
        this._updateValueText();
    }

    _updateValueText(){
        this.el.textDisplay.value = this.value;
        this.el.textDisplay.classList.remove("pin-login__text--error")
        if (this.value.length == 6){
            this._attemptLogin()
        }
    }

    _attemptLogin(){
        if (this.value == this.password && this.retimes == 3){
            console.log("you got in!")
            this._createDiv2()
            this.retimes = 1;
            this.el.textDisplay.value = this.value;
            this.value = this.value.substring(0, this.value.length - 6);
        }else if (this.value == this.password){
            this.retimes += 1
            console.log("you got in!")
            this._createDiv()
            this.el.textDisplay.value = this.value;
            this.value = this.value.substring(0, this.value.length - 6)
        }else{
            console.log("get out of here")
            this.el.textDisplay.classList.add("pin-login__text--error")
            this.value = this.value.substring(0, this.value.length - 6);
        }
    }
    
    _randPass(){
        var passward = "";
        var i;
        for (i = 0; i < 6; i++) {
        passward = passward.concat(parseInt(Math.random()*10).toString());
        }
        return passward;
    }

}

function getPos(el) {
    // yay readability
    for (var lx=0, ly=0;
         el != null;
         lx += el.offsetLeft, ly += el.offsetTop, el = el.offsetParent);
    return {x: lx,y: ly};
}
