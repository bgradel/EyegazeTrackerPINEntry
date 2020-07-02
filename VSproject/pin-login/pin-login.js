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
        
        const coord = [["853px","853px"],["629px","982px"],["371px","982px"],["147px","853px"],["18px","371px"],["18px","629px"],["147px","147px"],["371px","18px"],["629px","18px"],["853px","147px"]]
        const coord_testing = [["1034px","557px"],["698px","637px"],["362px","637px"],["27px","562px"],["-230px","400px"],["-403px","237px"],["-490px","77px"],["-500px","0px"],["-510px","0px"],["-523px","77px"]]
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
            keyEl.style.cssText = "position:relative; border:1px solid blue;";
            keyEl.style.left = coord_testing[i][0];
            keyEl.style.top =  coord_testing[i][1];
            i = i + 1;
        });

    }


    _handleKeyPress(key){
        if (this.value.length < this.maxNumbers && !isNaN(key)){
            this.value += key;
        }
        console.log(this.value)
        this._updateValueText();
    }

    _updateValueText(){
        this.el.textDisplay.value = this.value;
        this.el.textDisplay.classList.remove("pin-login__text--error")
        if (this.value.length == 4){
            this._attemptLogin()
        }
    }

    _attemptLogin(){
        if (this.value == "0404"){
            console.log("you got in!")
            window.location.href = this.redirectTo;
        }else{
            console.log("get out of here")
            this.el.textDisplay.classList.add("pin-login__text--error")
            this.value = this.value.substring(0, this.value.length - 4);
        }
    }

}