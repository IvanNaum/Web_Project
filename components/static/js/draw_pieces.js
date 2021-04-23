function drawPieces(pieces, black, white, user_color) {
    pieces.forEach(element => {
        color = element.color;
        row = element.row;
        col = element.col;

        var cell = document.getElementById(`${row}-${col}`);
        // Clear cell
        cell.innerHTML = "";

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