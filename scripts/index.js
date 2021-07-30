// On load: obtain gallery root and rearrange images
const gallery = document.querySelector(".posts");
arrangeGallery(gallery, false);

// On shuffle: force rearrangement of images
const shuffleButton = document.querySelector("#gal-shuffle");
shuffleButton.addEventListener("click", () => arrangeGallery(gallery, true));

// arranges the gallery in a shuffled order, maintaining the order throughout a single session
// set forceNew to force a new shuffle order in the same session. 
function arrangeGallery(root, forceNew) {
    let sequence = JSON.parse(sessionStorage.getItem("gallerySequence")); // correct sequence of id's
    numImages = root.childElementCount;
    if(!sequence || sequence.length != numImages || forceNew) {
        sequence = createRandomSequence(numImages);
        sessionStorage.setItem("gallerySequence", JSON.stringify(sequence));
    }

    // sort children based on correct sequence, and push to root
    Array.from(root.children)
        .sort( (a, b) => sequence.indexOf(Number(a.id)) - sequence.indexOf(Number(b.id)) )
        .forEach(child => root.append(child))
}

// get sequence of numbers from 0 to length - 1
// ex) [4, 6, 3, 2, 0, 1, 5] length 7
function createRandomSequence(length) {
    let list = [];
    for (let i = 0; i < length; i++) {
        list.push(i);
    }
    return shuffle(list);
}

// Fisher-Yates (Knuth) Shuffle
// https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
function shuffle(array) {
    var currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }