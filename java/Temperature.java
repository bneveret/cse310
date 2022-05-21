//Import tools for the display.
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Temperature {
    //Declare all the necessary variables for the frame'
    //Frame
    public static JFrame frmMain;

    //Labels
    public static JLabel lblCelsius;
    public static JLabel lblFahrenheit;

    //Text Fields
    public static JTextField textCelsius;
    public static JTextField textFahrenheit;

    //Buttons
    public static JButton btnCalculateCtoF;
    public static JButton btnCalculateFtoC;

    
    //Main Function
    public static void main (String[] args) {
        //Creates a new instance of temperature.
        Temperature temperature = new Temperature();

        //Create the frame and set it's size and layout.
        frmMain = new JFrame("Temperature Converter");
        frmMain.setSize(200,200);
        frmMain.setLayout(new FlowLayout());

        //Create the labels.
        lblCelsius = new JLabel("Celsius:");
        lblFahrenheit = new JLabel("Fahrenheit:");

        //create the text fields
        textCelsius = new JTextField(12);
        textFahrenheit = new JTextField(12);

        //create the Celsius to Fahrenheit button.
        btnCalculateCtoF = new JButton("Convert C to F");
        
        //add an event listener to detect when the button is clicked.
        btnCalculateCtoF.addActionListener(
            new ActionListener(){

                //convert Celsius to Fahrenheit when the button is clicked.
                public void actionPerformed(ActionEvent e){
                    String cText = textCelsius.getText();
                    double c = Double.parseDouble(cText);
                    double f = temperature.toFahrenheit(c);
                    
                    //change the text in the textFahrenheit text field.
                    textFahrenheit.setText(String.format("%.2f", f));
                }
            }  
        );

        //create the Fahrenheit to Celsius button.
        btnCalculateFtoC = new JButton("Convert F to C");

        //add an event listener to detect when the button is clicked.
        btnCalculateFtoC.addActionListener(
            new ActionListener(){

                //convert Fahrenheit to Celsius when the button is clicked.
                public void actionPerformed(ActionEvent e){
                    String fText = textFahrenheit.getText();
                    double f = Double.parseDouble(fText);
                    double c = temperature.toCelsius(f);

                    //change the text in the textCelsius text field.
                    textCelsius.setText(String.format("%.2f", c));
                }
            }
        );

        //add all of the frame elements to the display.
        frmMain.add(lblCelsius);
        frmMain.add(textCelsius);
        frmMain.add(lblFahrenheit);
        frmMain.add(textFahrenheit);
        frmMain.add(btnCalculateCtoF);
        frmMain.add(btnCalculateFtoC);

        //make the frame visible.
        frmMain.setVisible(true);
    }

    //function to convert Fahrenheit to Celsius
    public double toCelsius(double f) {
        double c;
        c = (f - 32.0) / 1.8;
        return c;
    }

    //function to convert Celsius to Fahrenheit
    public double toFahrenheit(double c) {
        double f;
        f = (c * 1.8) + 32.0;
        return f;
    }
}