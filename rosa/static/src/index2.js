
import { Water } from "/static/water/Water2.js";
var best_position_json_array = best_position_json["data"];
var best_position_json_vase = vase_best_position;
const position_vase_x = best_position_json_vase["position_vase_x"];
const position_vase_y = best_position_json_vase["position_vase_y"];
const position_vase_z = best_position_json_vase["position_vase_z"];
var loader = new THREE.GLTFLoader();

sndan(position_vase_x,position_vase_y,position_vase_z,0,0,0);

var water;
const params = {
  color: "#000",
  scale: 4,
  flowX: 1,
  flowY: 1,
};
//===================================================== full screen
var requestFullscreen = function (ele) {
  if (ele.requestFullscreen) {
    ele.requestFullscreen();
  } else if (ele.webkitRequestFullscreen) {
    ele.webkitRequestFullscreen();
  } else if (ele.mozRequestFullScreen) {
    ele.mozRequestFullScreen();
  } else if (ele.msRequestFullscreen) {
    ele.msRequestFullscreen();
  } else {
    console.log("Fullscreen API is not supported.");
  }
};
var exitFullscreen = function (ele) {
  if (ele.exitFullscreen) {
    ele.exitFullscreen();
  } else if (ele.webkitExitFullscreen) {
    ele.webkitExitFullscreen();
  } else if (ele.mozCancelFullScreen) {
    ele.mozCancelFullScreen();
  } else if (ele.msExitFullscreen) {
    ele.msExitFullscreen();
  } else {
    console.log("Fullscreen API is not supported.");
  }
};
//===================================================== add canvas
let renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0xd8e7ff, 0);
document.body.appendChild(renderer.domElement);
//===================================================== resize
window.addEventListener("resize", function () {
  let width = window.innerWidth;
  let height = window.innerHeight;
  renderer.setSize(width, height);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
});
//===================================================== add Scene
let scene = new THREE.Scene();
//===================================================== add Camera
let camera = new THREE.PerspectiveCamera(
  45,
  window.innerWidth / window.innerHeight,
  1,
  10000
);
let cameraTarget = new THREE.Vector3(0, 0, 0);
//===================================================== add Group
var group = new THREE.Group();
scene.add(group);
//===================================================== add Controls
var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;
//How far you can orbit vertically, upper and lower limits. The maximum is Pi / 2 (90deg). You wont see below the below the line of the horizon
controls.maxPolarAngle = Math.PI / 2.1;
//===================================================== add VR
renderer.setPixelRatio(window.devicePixelRatio); //VR
var effect = new THREE.StereoEffect(renderer); //VR
effect.setSize(window.innerWidth, window.innerHeight); //VR

var VR = false;

document.getElementById("VR").addEventListener("click", function () {
  toggleVR();
});

function toggleVR() {
  if (VR) {
    VR = false;
    controls = new THREE.OrbitControls(camera, renderer.domElement);
  } else {
    VR = true;
    controls = new THREE.DeviceOrientationControls(camera);
    requestFullscreen(document.documentElement);
  }
  renderer.setSize(window.innerWidth, window.innerHeight);
}

//===================================================== add lighta
var light = new THREE.DirectionalLight(0xefffff, 1.25);
light.position.set(1, 1, 1).normalize();
scene.add(light);
var light = new THREE.DirectionalLight(0xffefef, 2.25);
light.position.set(-1, -1, -1).normalize();
scene.add(light);

//Create a point light in our scene. Makes everything gloomy
var light = new THREE.PointLight(0xffffff, 1, 100);
scene.add(light);

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
add_water();

function add_water() {
  loader.load(
    "/static/water/watersndan1.glb",
    function (gltff) {
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

var model;

//===================================================== Loader
var clock = new THREE.Clock();
var mixer = null;
var firstObject;

var size = 0.05;
var meshList = [];

function PlaySound() {
  bflat.play();
}

//calculate distance of the main object
var firstBB = new THREE.Box3().setFromObject(group);

//calculate distance for all other objects
for (var i = 0; i < meshList.length; i++) {
  secondBB = new THREE.Box3().setFromObject(meshList[i]);
}

var count = 0;
function hit() {
  //recalculate distance for the main object
  firstBB = new THREE.Box3().setFromObject(group);
  //recalcuate distance for all the other objects
  for (var i = 0; i < meshList.length; i++) {
    secondBB = new THREE.Box3().setFromObject(meshList[i]);

    if (firstBB.isIntersectionBox(secondBB)) {
      PlaySound();
      info.style.color =
        "hsl(" + Math.floor(Math.random() * 290) + ",50%,50%)";
      info.innerHTML =
        Math.random() > 0.25
          ? "Superb!"
          : Math.random() > 0.25
          ? "Oustanding!"
          : "Awesome!";

      TweenLite.to(info, 0.75, {
        css: { fontSize: "50px", opacity: 1 },
        ease: Power4.easeOut,
        onComplete: function () {
          TweenLite.to(info, 0.75, {
            css: { fontSize: "14px", opacity: 0 },
            ease: Power4.easeOut,
          }); //end tween
        }, //end onComplete
      }); //end tween
    } //end if
  } //end for
} //end hit

//===================================================== bloom
var renderScene = new THREE.RenderPass(scene, camera);
var shaderActive = "none";
var gui = new dat.GUI();
dat.GUI.toggleHide();
var composer;

var parameters = {
  x: 0,
  y: 30,
  z: 0,
  bloomStrength: 1.0,
  bloomRadius: 1.0,
  bloomThreshold: 0.45,
  useShaderNone: function () {
    setupShaderNone();
  },
  useShaderBloom: function () {
    setupShaderBloom();
  },
};

gui.add(parameters, "useShaderNone").name("Display Original Scene");

var folderBloom = gui.addFolder("Bloom");
var bloomStrengthGUI = folderBloom
  .add(parameters, "bloomStrength")
  .min(0.0)
  .max(2.0)
  .step(0.01)
  .name("Strength")
  .listen();
bloomStrengthGUI.onChange(function (value) {
  setupShaderBloom();
});
var bloomRadiusGUI = folderBloom
  .add(parameters, "bloomRadius")
  .min(0.0)
  .max(5.0)
  .step(0.01)
  .name("Radius")
  .listen();
bloomRadiusGUI.onChange(function (value) {
  setupShaderBloom();
});
var bloomThresholdGUI = folderBloom
  .add(parameters, "bloomThreshold")
  .min(0)
  .max(0.99)
  .step(0.01)
  .name("Threshold")
  .listen();
bloomThresholdGUI.onChange(function (value) {
  setupShaderBloom();
});
folderBloom.add(parameters, "useShaderBloom").name("Use Bloom Shader");
folderBloom.open();

//===================================================== functions

function setupShaderNone() {
  shaderActive = "none";
}

function setupShaderBloom() {
  composer = new THREE.EffectComposer(renderer);
  composer.addPass(new THREE.RenderPass(scene, camera));

  /*unreal bloom*/
  var effectFXAA = new THREE.ShaderPass(THREE.FXAAShader);
  effectFXAA.uniforms["resolution"].value.set(
    1 / window.innerWidth,
    1 / window.innerHeight
  );

  var copyShader = new THREE.ShaderPass(THREE.CopyShader);
  copyShader.renderToScreen = true;

  var bloomPass = new THREE.UnrealBloomPass(
    new THREE.Vector2(window.innerWidth, window.innerHeight),
    parameters.bloomStrength,
    parameters.bloomRadius,
    parameters.bloomThreshold
  );

  composer = new THREE.EffectComposer(renderer);
  composer.setSize(window.innerWidth, window.innerHeight);
  composer.addPass(renderScene);
  composer.addPass(effectFXAA);
  composer.addPass(bloomPass);
  composer.addPass(copyShader);
  shaderActive = "bloom";
}

function isShaderActive() {
  if (shaderActive == "none") {
    renderer.render(scene, camera);
  } else {
    composer.render();
  }
}

//active bloom on load
setupShaderBloom();

//===================================================== Animate
var percentage = 0;
var prevTime = Date.now();

function animate() {
  hit();
  var delta = clock.getDelta();
  if (mixer != null) mixer.update(delta);

  //VR
  if (VR) {
    effect.render(scene, camera);
  } else {
    //renderer.render( scene, camera );
    isShaderActive();
  }

  requestAnimationFrame(animate);
  controls.update();
}
animate();

//set camera position
camera.position.x = 200;
camera.position.y = 50;
camera.position.z = 50;