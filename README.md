# FLC (Fuzzy Logic Control) / FIS (Fuzzy Inference System)

Code for FLC/FIS:
- 2 inputs (error and delta error)
- 1 output (motor speed)
- MISO (Multi Inputs Single Output)

Context:
- A fuzzy logic controller is used to manage the speed of a motor (in RPM) based on the measurement of current error and delta error with certain membership functions.
- Computation in one forward pass only.

Further developments:
- Add incremental error input
- Add more fuzzy sets on each fuzzy variable
- MIMO (Multi Inputs Multi Outputs) --> e.g. controlling voltage excitation for UVW lines of a 3-phase motor.

Credits:
- Coded by Gredynov Sitanggang (23/531185/PPA/06761), MSc student in electronics and instrumentation, Universitas Gadjah Mada.
- Based on the mid-term project of the Intelligent Control System course taught by Dr. Oskar Natan.
