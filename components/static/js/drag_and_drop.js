(function dragDrop() {
    const piecesElements = document.querySelectorAll(".piece");
    const blacksElements = document.querySelectorAll(".black");

    let element;

    piecesElements.forEach(elem => {
        elem.draggable = true;

        elem.addEventListener("dragstart", (e => {
            e.dataTransfer.setData("text/html", "dragstart");
            element = e.target
        }));
        // elem.addEventListener("drag", (e => {
        //     console.log('drag')
        // }));
        // elem.addEventListener("dragend", (e => {
        //     console.log('dragend')
        // }));
    })
    blacksElements.forEach(elem => {
        // elem.addEventListener("dragenter", (e => {
        //     console.log('dragenter')
        // }));
        elem.addEventListener("dragover", (e => {
            e.preventDefault();
        }));
        elem.addEventListener("drop", (e => {
            if (!e.target.innerHTML.trim() && e.target.classList.contains('black')) {
                e.target.appendChild(element);
            }
        }));
    })
})();

