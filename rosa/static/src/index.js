"use strict";
import * as THREE from "/static/src/three.module.js";
import { OrbitControls } from "/static/src/OrbitControls.js";
import { Water } from "/static/src/Water.js";
import { GLTFLoader } from "/static/src/GLTFLoader.js";
import { RGBELoader } from '/static/src/RGBELoader.js';
var container;
var camera, scene, renderer;
var numberrose1=0;
var myTimeout;
var camera, scene, renderer;
var loader = new GLTFLoader(); 
var best_position_json_array = best_position_json["data"];
var best_position_json_vase = vase_best_position;
const position_vase_x = best_position_json_vase["position_vase_x"];
const position_vase_y = best_position_json_vase["position_vase_y"];
const position_vase_z = best_position_json_vase["position_vase_z"];
/*const rotation_vase_x = best_position_json_vase["rotation_vase_x"];
const rotation_vase_y = best_position_json_vase["rotation_vase_y"];
const rotation_vase_z = best_position_json_vase["rotation_vase_z"];*/

sndan(position_vase_x,position_vase_y,position_vase_z,0,0,0);

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
  console.log(array_of_flowers[flower_index])
 rose1(array_of_flowers[flower_index], best_position_json_array[flower_index]['positionX'] ,best_position_json_array[flower_index]['positinY'] ,best_position_json_array[flower_index]['positinZ'],best_position_json_array[flower_index]['rotationX'],best_position_json_array[flower_index]['rotationY'],best_position_json_array[flower_index]['rotationZ'],array_of_flowers.length) ;
}
async function  rose1(flower_object_url,pox,poy,poz,rox,roy,roz,lngthdata) {
      await loader.load( flower_object_url , function (gltff) {
      gltff.scene.children[0].traverse(function (child) {
        if (child.isMesh) {
        console.log(child.name)
          /* --- Set position dataset of flower --- */
          child.position.x=pox
          child.position.y=poy
          child.position.z=poz
          child.rotation.x= rox
          child.rotation.y= roy
          console.log(roz)
          child.rotation.z= roz
          scene.add(child);
        }
      });
    }, (xhr) => {
    }, (error) => {
      console.log("error");

    }); 
  }
  function sndan(pox,poy,poz,rox,roy,roz) {
    loader.load(vase_object, function (gltffsnd) {
      gltffsnd.scene.children[0].traverse(function (childsndan) {
        if (childsndan.isMesh) {
          /* --- Set position dataset of vase --- */
          childsndan.position.x=pox
          childsndan.position.y=poy 
          childsndan.position.z=poz
          childsndan.rotation.x= rox
          childsndan.rotation.y= roy
          childsndan.rotation.z= roz
          /* --- Set material properity --- */
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
  /* --- Create WebGLRendered --- */
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
   .setPath('/static/src/textures/equirectangular/')
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

domen();

function domen() {
  loader.load(
    "/static/src/textures/ball.glb",
    function (gltff) {
      console.log(loader1.onProgress);
      //face1.glb
      console.log(gltff.scene);
      gltff.scene.traverse(function (child) {
        if (child.isMesh) {
          child.receiveShadow = true;
          child.castShadow = true;

          //  scene.add(child);

          const waterGeometry = new THREE.SphereGeometry(5, 5, 5);

          water = new Water(child.geometry, {
            color: params.color,
            scale: params.scale,
            flowDirection: new THREE.Vector2(params.flowX, params.flowY),
            textureWidth: 1024,
            textureHeight: 1024,
            transprant: true,
            opacity: 0.5,
          });

          //water.position.y = 1;
          //	water.rotation.x = Math.PI * - 0.5;
          scene.add(water);
        }
      });
    },
    (xhr) => {
      if ((xhr.loaded / xhr.total) * 100 == 100) {
      }
      console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
    },
    (error) => {
      console.log(error);
    }
  );
}