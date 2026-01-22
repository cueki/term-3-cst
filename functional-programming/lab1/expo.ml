(* Madison Lovett, A01292253
   Jan 21, 2026 *)

(* Computes an approximation of e^x using the Taylor series expansion.
   exp(x) = 1 + x + x^2/2! + x^3/3! + x^4/4! + ...*)
let expo num_terms x =
    let rec aux index current_term acc =
        if index >= num_terms then acc
        else
            let next_term = current_term *. x /. float_of_int index in
            aux (index + 1) next_term (acc +. next_term)
    in
    if num_terms < 1 then 0.0
    else aux 1 1.0 1.0

