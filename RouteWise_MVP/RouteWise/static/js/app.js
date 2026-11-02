const svg = document.getElementById("network");
const startSelect = document.getElementById("start");
const goalSelect = document.getElementById("goal");
const button = document.getElementById("findRoute");
const NS = "http://www.w3.org/2000/svg";

let locations = [];
let edges = [
  ["uran","panvel"],["panvel","kharghar"],["panvel","belapur"],
  ["kharghar","belapur"],["kharghar","nerul"],["belapur","nerul"],
  ["nerul","vashi"],["vashi","koparkhairane"],["koparkhairane","airoli"]
];

function el(tag, attrs={}, text="") {
  const node = document.createElementNS(NS, tag);
  Object.entries(attrs).forEach(([k,v]) => node.setAttribute(k,v));
  if (text) node.textContent = text;
  return node;
}
function draw(path=[]) {
  svg.innerHTML = "";
  const routeEdges = new Set();
  for(let i=0;i<path.length-1;i++) routeEdges.add([path[i],path[i+1]].sort().join("|"));
  edges.forEach(([a,b]) => {
    const p = locations.find(x=>x.id===a), q = locations.find(x=>x.id===b);
    if(!p||!q) return;
    const key=[a,b].sort().join("|");
    svg.appendChild(el("line",{x1:p.x,y1:p.y,x2:q.x,y2:q.y,class:routeEdges.has(key)?"edge active":"edge"}));
  });
  locations.forEach(p => {
    const group=el("g",{class:"node"+(path.includes(p.id)?" selected":"")});
    group.appendChild(el("circle",{cx:p.x,cy:p.y,r:9}));
    group.appendChild(el("text",{x:p.x,y:p.y-17},p.name));
    svg.appendChild(group);
  });
}
async function loadLocations(){
  const res=await fetch("/api/locations");
  locations=await res.json();
  draw();
}
button.addEventListener("click", async()=>{
  const error=document.getElementById("error");
  error.textContent="";
  button.disabled=true; button.textContent="Calculating...";
  try{
    const response=await fetch("/api/route",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({start:startSelect.value,goal:goalSelect.value})});
    const data=await response.json();
    if(!response.ok) throw new Error(data.error||"Could not calculate route.");
    document.getElementById("results").classList.remove("hidden");
    document.getElementById("dDistance").textContent=data.dijkstra.distance+" km";
    document.getElementById("aDistance").textContent=data.astar.distance+" km";
    document.getElementById("dPath").textContent=data.dijkstra.names.join("  →  ");
    document.getElementById("aPath").textContent=data.astar.names.join("  →  ");
    document.getElementById("dVisited").textContent=data.dijkstra.visited;
    document.getElementById("aVisited").textContent=data.astar.visited;
    document.getElementById("note").textContent=data.note;
    draw(data.dijkstra.path);
    document.getElementById("results").scrollIntoView({behavior:"smooth",block:"start"});
  }catch(err){error.textContent=err.message;}
  finally{button.disabled=false;button.innerHTML='Calculate best route <span>↗</span>';}
});
loadLocations().catch(()=>{document.getElementById("error").textContent="Could not load the route network. Please refresh.";});
