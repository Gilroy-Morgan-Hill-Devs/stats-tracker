
// is declaring a global variable/function bad practice?
// does this pollute the global scope?
var flipCoin = function() {
	/*
		generates random coin flip. Adds class to coin
	*/

	clearClass();
	var result = Math.floor(Math.random() * 2);
	result = result ? "heads" : "tails";

	// need a delay in state change for transition animation
	setTimeout(function() {
		document.querySelector("#coin").classList.add(result);
	}, 100);
};

var clearClass = function() {
	/*
		clears heads/tails class from coin
	*/

	// replace original node with a clone that has cleared classes
	// to prevent transition animation from occuring
	var elm = document.getElementById("coin");
	var newone = elm.cloneNode(true);
	//remove classes
	newone.classList.remove("heads");
	newone.classList.remove("tails");
	elm.parentNode.replaceChild(newone, elm);
}