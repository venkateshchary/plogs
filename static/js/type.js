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
            this.writeSequence(this.sequences[this.seqCount], this);
        }
    }

    writeSequence(sequence, writer){
        if (sequence.writeLen < sequence.text.length){
            let elmnt = document.getElementById("line-1");
            elmnt.innerHTML += sequence.text.charAt(sequence.writeLen);
            sequence.writeLen++;
            setTimeout(function(){writer.writeSequence(sequence, writer);}, sequence.speed);
        }
        else{
            writer.seqCount++;
            writer.write();
        }
    }

}


document.addEventListener("DOMContentLoaded", function(){
    let seqs = [
        new Sequence('1', 100, 100, null, null),
        new Sequence('2', 100, 100, null, null)
    ];

    let writer = new TypeWriter(seqs);
    writer.write();
});
