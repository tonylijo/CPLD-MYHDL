module tb_full_adder;

reg A;
reg B;
reg C_in;
wire Sum_out;
wire C_out;

initial begin
    $from_myhdl(
        A,
        B,
        C_in
    );
    $to_myhdl(
        Sum_out,
        C_out
    );
end

full_adder dut(
    A,
    B,
    C_in,
    Sum_out,
    C_out
);

endmodule
