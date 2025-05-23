#!/usr/bin/gnuplot

# Set terminal for PNG output
set terminal pngcairo enhanced color size 1200,800 font 'Arial,12'
set output 'shock_tube_results.png'

# Set up multiplot layout
set multiplot layout 2,2 title "Shock Tube Results at t=0.007s"

# Temperature plot
set title "Temperature Distribution"
set xlabel "Position (m)"
set ylabel "Temperature (K)"
set grid
plot 'postProcessing/temperatureSampling/0.007/data_T.csv' using 1:2 with lines linewidth 2 title 'Temperature'

# Pressure plot  
set title "Pressure Distribution"
set xlabel "Position (m)"
set ylabel "Pressure (Pa)"
set grid
plot 'postProcessing/pressureSampling/0.007/data_p.csv' using 1:2 with lines linewidth 2 title 'Pressure'

# Velocity magnitude plot
set title "Velocity Magnitude"
set xlabel "Position (m)"
set ylabel "Velocity (m/s)"
set grid
plot 'postProcessing/velocitySampling/0.007/data_U.csv' using 1:(sqrt($2*$2+$3*$3+$4*$4)) with lines linewidth 2 title '|U|'

# Combined normalized plot
set title "All Fields (Normalized)"
set xlabel "Position (m)"
set ylabel "Normalized Values"
set grid
plot 'postProcessing/temperatureSampling/0.007/data_T.csv' using 1:($2/348.432) with lines linewidth 2 title 'T (norm)', \
     'postProcessing/pressureSampling/0.007/data_p.csv' using 1:($2/100000) with lines linewidth 2 title 'p (norm)'

unset multiplot
