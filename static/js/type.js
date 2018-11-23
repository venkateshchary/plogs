class Sequence{

    constructor(text, speed, color, elementId){
        this.text = text;
        this.speed = speed;
        this.color = color;
        this.elementId = elementId;

        // keeps track of how much text has been written on screen
        this.writeLen = 0;
    }
}


class TypeWriter{

    constructor(sequences){
        this.sequences = sequences;
    }

	write(){
	    if(this.sequences == null || this.sequences.length == 0)
	        return;

        function writeSequence(sequence){
            if (sequence.writeLen < sequence.text.length){
                let elmnt = document.getElementById("line-1");
                elmnt.innerHTML += sequence.text.charAt(sequence.writeLen);
                sequence.writeLen++;
                setTimeout(function(){writeSequence(sequence);}, sequence.speed);
            }
        }


        let cur_seq = this.sequences[0];
        writeSequence(cur_seq);
    }
}


document.addEventListener("DOMContentLoaded", function(){
    let seq = new Sequence('pip3 install plogs', 100, null);
    let writer = new TypeWriter([seq]);
    writer.write();
});
