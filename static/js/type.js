let term_element = document.getElementById("term");

function createLine(term_icon, line_count){
    let term_cont = document.createElement("div");
    term_cont.setAttribute("class", "term-cont");

    let term_line = document.createElement("div");
    term_line.setAttribute("class", "term-line");

    let term_prompt = document.createElement("span");
    term_prompt.setAttribute("class", "term-prompt");
    term_prompt.innerHTML = term_icon;

    let term_cmd = document.createElement("span");
    term_cmd.setAttribute("class", "term-cmd current");
    term_cmd.id = line_count.toString();

    let term_caret = document.createElement("span");
    term_caret.setAttribute("class", "term-caret");
    term_caret.innerHTML="&#x2588";

    term_line.appendChild(term_prompt);
    term_line.appendChild(term_cmd);
    term_line.appendChild(term_caret);
    term_cont.appendChild(term_line);

    return term_cont;
}

class Sequence{

    constructor(text, speed, delay, color, elementId){
        this.text = text;
        this.speed = speed;
        this.delay = delay;
        this.color = color;
        this.elementId = elementId;

        // keeps track of how much text has been written on screen
        this.writeLen = 0;
    }
}


class TypeWriter{

    constructor(sequences){
        this.sequences = sequences;
        this.seqCount = 0;
    }

    write(){
	    if(this.sequences == null || this.sequences.length == 0)
	        return;

        if(this.seqCount < this.sequences.length){

            // create new line and append it to terminal
            let new_line = createLine(" $ ", this.seqCount);
            document.getElementById("term").appendChild(new_line);

            // get element where we write text too
            let term_text = document.getElementById(this.seqCount);

            // write sequence to new line
            this.writeSequence(this.sequences[this.seqCount], term_text, this);
        }
    }

    writeSequence(sequence, term_text, writer){

        if (sequence.writeLen < sequence.text.length){
            // update line we write text too
            term_text.innerHTML += sequence.text.charAt(sequence.writeLen);

            sequence.writeLen++;
            setTimeout(function(){writer.writeSequence(sequence, term_text, writer);}, sequence.speed);
        }
        else{
            writer.seqCount++;
            writer.write();
        }
    }

}


document.addEventListener("DOMContentLoaded", function(){

    let seqs = [
        new Sequence('pip3 install plogs', 100, 100, null, null)
        //new Sequence('python3', 100, 100, null, null)
    ];

    let writer = new TypeWriter(seqs);
    writer.write();
});
