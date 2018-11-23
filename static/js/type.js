function main(){
    setInterval(caretToggle, 500);

    function caretToggle() {
        let caret = document.getElementsByClassName("term-caret")[0];
        if (caret.classList.contains('blink'))
            caret.classList.remove('blink');
        else
            caret.classList.add('blink');
    }

    let term_inp = document.getElementsByClassName('term-input-hide')[0]
    let term_cmd = document.getElementsByClassName('term-cmd')[0];
    term_inp.addEventListener("keyup", typeCommand);

    function typeCommand(e) {
      console.log(e)
      let v = term_inp.value;
      term_cmd.innerHTML = v;
    }

    //let term = document.getElementById('term');
    //term.addEventListener("click", term_inp.focus())
}

window.onload = function(){
    main();
}
