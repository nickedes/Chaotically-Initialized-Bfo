**SPHERE**

Fitness Function - SPHERE

*Information about files:*

1. `init.py` - Initialization of all the paramters and space.
2. `optimization.py` - Contains all the steps of Bfo Alog.
3. `bfo.py` - Combining inits with the algo and saving results.
4. `data.py` - Saved all the results in the form of dictionary.
5. `results.json` - A `JSON` file obtained from the `data.py`.
6. `jsontohtml.py` - A python script that changes `JSON` to `Html`.
7. `result.html` - `Html` obtained from `jsontohtml.py` has a table representation of the data.
8. `maps.py` - Contains all the Chaotic maps used, instead of random initializations.

<!-- ![Table](result.html) -->
#Results

<table>
  <thead>
    <tr>
      <th>Maps</th>
      <th>logistic</th>
      <th>chebyshev</th>
      <th>gauss</th>
      <th>piecewise</th>
      <th>singer</th>
      <th>tent</th>
      <th>iterative</th>
      <th>sine</th>
      <th>circle</th>
      <th>sinusoidal</th>
      <th>c_prob</th>
      <th>c_space</th>
      <th>c_tumble</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cspace</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1.482197e-323</td>
      <td>0.001151</td>
      <td>1.000000e+00</td>
      <td>0.011319</td>
      <td>0.028613</td>
      <td>0.004145</td>
      <td>8.034325e-07</td>
      <td>2.786120e-09</td>
      <td>0.040819</td>
      <td>1.590702e-32</td>
      <td>0.8</td>
      <td>0.1</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.446591e-323</td>
      <td>0.000304</td>
      <td>1.000000e+00</td>
      <td>1.250000</td>
      <td>0.078825</td>
      <td>0.008671</td>
      <td>4.105622e-06</td>
      <td>1.254784e-09</td>
      <td>0.041701</td>
      <td>2.209726e-137</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6.916919e-323</td>
      <td>0.001035</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.462510e-05</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>cprob</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.916919e-323</td>
      <td>0.001178</td>
      <td>3.155444e-30</td>
      <td>0.012236</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>8.613881e-06</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.916919e-323</td>
      <td>0.000809</td>
      <td>3.155444e-30</td>
      <td>0.012236</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>4.040380e-05</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.5</td>
      <td>0.3</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.916919e-323</td>
      <td>0.001035</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.462510e-05</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>ctumble</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.916919e-323</td>
      <td>0.000008</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.353021e-04</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6.916919e-323</td>
      <td>0.000028</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.238547e-05</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6.916919e-323</td>
      <td>0.012476</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.255987e-03</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>cspace and cprob</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.482197e-323</td>
      <td>0.003034</td>
      <td>1.000000e+00</td>
      <td>0.012235</td>
      <td>0.028613</td>
      <td>0.004145</td>
      <td>3.718179e-04</td>
      <td>2.786120e-09</td>
      <td>0.040819</td>
      <td>1.590702e-32</td>
      <td>0.2</td>
      <td>0.1</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.446591e-323</td>
      <td>0.332180</td>
      <td>1.000000e+00</td>
      <td>1.250000</td>
      <td>0.078825</td>
      <td>0.008671</td>
      <td>3.844106e-03</td>
      <td>1.254784e-09</td>
      <td>0.041701</td>
      <td>2.209726e-137</td>
      <td>0.5</td>
      <td>0.2</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>11</th>
      <td>6.916919e-323</td>
      <td>0.012476</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.255987e-03</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>cspace and ctumble</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.482197e-323</td>
      <td>0.000038</td>
      <td>1.000000e+00</td>
      <td>0.011319</td>
      <td>0.028613</td>
      <td>0.004145</td>
      <td>1.671792e-05</td>
      <td>2.786120e-09</td>
      <td>0.040819</td>
      <td>1.590702e-32</td>
      <td>0.8</td>
      <td>0.1</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.446591e-323</td>
      <td>0.000007</td>
      <td>1.000000e+00</td>
      <td>1.250000</td>
      <td>0.078825</td>
      <td>0.008671</td>
      <td>4.351960e-05</td>
      <td>1.254784e-09</td>
      <td>0.041701</td>
      <td>2.209726e-137</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>0.30</td>
    </tr>
    <tr>
      <th>14</th>
      <td>6.916919e-323</td>
      <td>0.012476</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.255987e-03</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>cprob and ctumble</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6.916919e-323</td>
      <td>0.000063</td>
      <td>3.155444e-30</td>
      <td>0.012236</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.382950e-04</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>16</th>
      <td>6.916919e-323</td>
      <td>0.000024</td>
      <td>3.155444e-30</td>
      <td>0.012236</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>5.224183e-05</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.5</td>
      <td>0.3</td>
      <td>0.30</td>
    </tr>
    <tr>
      <th>17</th>
      <td>6.916919e-323</td>
      <td>0.012476</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.255987e-03</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>cspace, cprob and ctumble</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.482197e-323</td>
      <td>0.000052</td>
      <td>1.000000e+00</td>
      <td>0.012235</td>
      <td>0.028613</td>
      <td>0.004145</td>
      <td>1.671792e-05</td>
      <td>2.786120e-09</td>
      <td>0.040819</td>
      <td>1.590702e-32</td>
      <td>0.2</td>
      <td>0.1</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>19</th>
      <td>4.446591e-323</td>
      <td>0.000014</td>
      <td>1.000000e+00</td>
      <td>1.250000</td>
      <td>0.078825</td>
      <td>0.008671</td>
      <td>4.463607e-06</td>
      <td>1.254784e-09</td>
      <td>0.041701</td>
      <td>2.209726e-137</td>
      <td>0.5</td>
      <td>0.2</td>
      <td>0.30</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6.916919e-323</td>
      <td>0.012476</td>
      <td>3.155444e-30</td>
      <td>0.000985</td>
      <td>0.032476</td>
      <td>0.000043</td>
      <td>1.255987e-03</td>
      <td>2.290225e-09</td>
      <td>0.040670</td>
      <td>7.603337e-59</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>0.50</td>
    </tr>
  </tbody>
</table>