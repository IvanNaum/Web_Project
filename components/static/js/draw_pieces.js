function drawPieces(pieces, black, white, user_color) {

    // Clear board
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            var cell = document.getElementById(`${i}-${j}`);
            cell.innerHTML = "";
        }   
    }

    // Draw new pieces
    pieces.forEach(element => {
        color = element.color;
        row = element.row;
        col = element.col;

        var cell = document.getElementById(`${row}-${col}`);

        var piece = document.createElement("div");

        if (color == user_color) {
            piece.className += "piece ";
        };

        if (color == black) {
            piece.className += "bg-blue-500 text-white ";
        } else if (color == white) {
            piece.className += "bg-white text-black ";
        };

        piece.className += "flex justify-center items-center w-5/6 h-5/6 rounded-full ";

        cell.appendChild(piece);
    });
};