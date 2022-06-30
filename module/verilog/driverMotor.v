`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/19/2022 09:57:49 PM
// Design Name: 
// Module Name: driverMotor
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module driverMotor(
    input wire clk,
    input wire ena,
    input wire [1:0] inSnr,
    output reg [1:0] statusM,
    //output reg [1:0] status2,
    output reg [1:0] move

    );
    
    reg [1:0] cntr;
    
    always @(*)
begin

    statusM = 0;
    move = 1;
    
    statusM = inSnr;
    cntr[1] = inSnr[1] & ena;
    cntr[0] = inSnr[0] & ena;
    move = cntr;
    //status2 = cntr; 
       
end
    
endmodule

