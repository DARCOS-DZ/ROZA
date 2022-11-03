"use strict";
import * as THREE from "/static/src/three.module.js";
import { OrbitControls } from "/static/src/OrbitControls.js";
import { GLTFLoader } from "/static/src/GLTFLoader.js";
import { RGBELoader } from '/static/src/RGBELoader.js';
var container;
var camera, scene, renderer
var numberrose1=0
var myTimeout;
var loader = new GLTFLoader(); 
var camera, scene, renderer;
var loader = new GLTFLoader(); 
sndan()
var best_position_json_array = best_position_json["data"];
//console.log(best_position_json["data"])
  container = document.createElement("div");
  document.body.appendChild(container);
  // scene
  scene = new THREE.Scene();
  // camera
  camera = new THREE.PerspectiveCamera(
    30,
    window.innerWidth / window.innerHeight,
    1,
    10000
  );
  camera.position.set(
    0,
    0,
   600
  );
 
 		
  /*fetch('/static/vases.json').then(async function (response) {
    return await response.json();
  }).then( function  (data) {
    function icrenum(num){
     }
     try {setInterval( function (){  rose1(data.data[numberrose1]?.name,data.data[numberrose1]?.positionX,data.data[numberrose1]?.positinY,data.data[numberrose1]?.positinZ,data.data[numberrose1]?.rotationX,data.data[numberrose1]?.rotationY,data.data[numberrose1]?.rotationZ,data.data.length) ;icrenum(numberrose1++)}, 200);}
     catch {
      console.log("rrr")
     }
  }).catch(function (err) {
    console.warn('Something went wrong.', err);
  });*/
for(let flower_index=0;flower_index<array_of_flowers.length;flower_index++){
 rose1(array_of_flowers[flower_index], best_position_json_array[flower_index]['positionX'] ,best_position_json_array[flower_index]['positinY'] ,best_position_json_array[flower_index]['positinZ'],best_position_json_array[flower_index]['rotationX'],best_position_json_array[flower_index]['rotationY'],best_position_json_array[flower_index]['rotationZ'],array_of_flowers.length) ;
}
var tomixerloop=0;     
//var tomixerloop=0;
function  rose1(nam,pox,poy,poz,rox,roy,roz,lngthdata) {
 // if (nam != undefined && nam != null) {
     // loader.load('/static/models/rose1/' + nam + '.glb', function (gltff) {
      loader.load( nam , function (gltff) {
      gltff.scene.children[0].traverse(function (child) {
        if (child.isMesh) {
            child.position.x=pox
            child.position.y=poy 
            child.position.z=poz
            child.rotation.z= roz
            child.rotation.x= rox
            child.rotation.y= roy
            scene.add(child);
            if(numberrose1==lngthdata-1){
              clearInterval(myTimeout)
            }
        }
      });
    }, (xhr) => {
    }, (error) => {
    }); 
 // }

  }
  function sndan() {
    loader.load(vase_object, function (gltffsnd) {
      //face1.glb
      gltffsnd.scene.children[0].traverse(function (childsndan) {
        if (childsndan.isMesh) {
          childsndan.material.metalness = 0.9;
          childsndan.material.roughness = 0.02;
          childsndan.material.exposure = 0.1;
          childsndan.receiveShadow = true;
          childsndan.castShadow = true;
          //  childsndan.material.flatShading = true;
          childsndan.material.transparent = true;
          childsndan.material.opacity = 0.5;
          scene.add(childsndan);

        }
      });
    }, (xhr) => {
    }, (error) => {
    });
  }
  renderer = new THREE.WebGLRenderer({ antialias: true,alpha: true });
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  container.appendChild(renderer.domElement);
  renderer.gammaInput = true;
  renderer.gammaOutput = true;
  renderer.shadowMap.enabled = true;
  var controls = new OrbitControls(camera, renderer.domElement);

  window.addEventListener("resize", onWindowResize, false);

 const pmremGenerator = new THREE.PMREMGenerator(renderer);
 pmremGenerator.compileEquirectangularShader();
 new RGBELoader()
   .setDataType(THREE.UnsignedByteType)
   .setPath('/static/textures/equirectangular/')
   .load('studio_small_08_1k.hdr', function (texture) {
     const envMap = pmremGenerator.fromEquirectangular(texture).texture;
     scene.environment = envMap;
     texture.dispose();
     pmremGenerator.dispose();
     render();
   });
function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize(window.innerWidth, window.innerHeight);
 
}
var clock5=new THREE.Clock();
function update() {
  camera.updateProjectionMatrix();
}
//
animate();
function animate() {
  requestAnimationFrame(animate);
  update();
  render();
  
}
function render() {   
  renderer.render(scene, camera);

}
