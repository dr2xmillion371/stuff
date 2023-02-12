<!DOCTYPE html>
<html>
<body>

// head
<h2>Bashicu matrix list</h2>

<p id="demo"></p>

// list
<script>
const bm = ["(0)", "(0)(0)", "(0)(0)(0)", "(0)(0)(0)(0)", "(0)(0)(0)(0)(0)", "(0)(1)"];

let text = "";
for (let i = 0; i < bm.length; i++) {
  text += bm[i] + "<br>";
}

document.getElementById("demo").innerHTML = text;
</script>

</body>
</html>
