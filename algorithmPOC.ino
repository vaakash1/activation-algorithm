// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
static const int samples = 15;
using namespace std;
int pointer;
double accelerations[samples];
long times[samples];
void setup(void) {
  //All magnitudes of accelerations collected in initial trials
  pointer = 0;
  Serial.begin(115200);
  while (!Serial)
    delay(10);  // will pause Zero, Leonardo, etc until serial console opens


  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  /*
  switch (mpu.getAccelerometerRange()) {
    case MPU6050_RANGE_2_G:
      Serial.println("+-2G");
      break;
    case MPU6050_RANGE_4_G:
      Serial.println("+-4G");
      break;
    case MPU6050_RANGE_8_G:
      Serial.println("+-8G");
      break;
    case MPU6050_RANGE_16_G:
      Serial.println("+-16G");
      break;
  }*/
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  /*
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
    case MPU6050_RANGE_250_DEG:
      Serial.println("+- 250 deg/s");
      break;
    case MPU6050_RANGE_500_DEG:
      Serial.println("+- 500 deg/s");
      break;
    case MPU6050_RANGE_1000_DEG:
      Serial.println("+- 1000 deg/s");
      break;
    case MPU6050_RANGE_2000_DEG:
      Serial.println("+- 2000 deg/s");
      break;
  }*/

  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  /*
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
    case MPU6050_BAND_260_HZ:
      Serial.println("260 Hz");
      break;
    case MPU6050_BAND_184_HZ:
      Serial.println("184 Hz");
      break;
    case MPU6050_BAND_94_HZ:
      Serial.println("94 Hz");
      break;
    case MPU6050_BAND_44_HZ:
      Serial.println("44 Hz");
      break;
    case MPU6050_BAND_21_HZ:
      Serial.println("21 Hz");
      break;
    case MPU6050_BAND_10_HZ:
      Serial.println("10 Hz");
      break;
    case MPU6050_BAND_5_HZ:
      Serial.println("5 Hz");
      break;
  }*/
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println("");
  delay(100);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  double testArr1[15] = { 0, 1, 2, 4, 5, 1, 3, 0.984, 2, 2, 1, 3, 0.984, 2, 2};
  Serial.println(allUnderValue(testArr1, 5.1));
}

void loop() {


  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  /*Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");*/
  double acceleration_magnitude = a.acceleration.x * a.acceleration.x + a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z;
  accelerations[pointer] = acceleration_magnitude;
  times[pointer] = millis;
  //Serial.print(acceleration_magnitude);
  if (simpleFalling(200, accelerations, times, pointer)/*acceleration_magnitude < 121 && acceleration_magnitude > 64*/) {
    digitalWrite(LED_BUILTIN, LOW);  // turn the LED on (HIGH is the voltage level)
    Serial.println("safe");
  } else {
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED off by making the voltage LOW
    Serial.println("not");
  }
  pointer++;
  pointer = pointer % 15;
}

bool allUnderValue(double arr[], double check) {
  for (int i = 0; i < samples; i++) {
    if (arr[i] > check) {
      return false;
    }
  }
  return true;
}


double getSlope(double arr_a[], long arr_t[], int indexAt, int depth){
    return (arr_a[indexAt] - arr_a[(indexAt - depth) % samples])/(arr_t[indexAt] - arr_t[(indexAt - depth) % samples]);
}

// length of accelerations must be 
bool simpleFalling(double max_a, double accelerations[samples], long times[samples], int pointer){
  if(getSlope(accelerations, times, pointer, 1) < -3){
    Serial.println(1);
    return true;
  }
  for(int i = pointer; i % samples != (pointer - 1) % 15; i++){
    if(accelerations[i] < max_a && allUnderValue(accelerations, max_a)){
      Serial.println(2);
      return true;        
    }
  }  
  return false;
}
