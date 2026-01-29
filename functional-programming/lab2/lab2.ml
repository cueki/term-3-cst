(* Madison Lovett, A01292253
   Jan 28, 2026 *)


(* map using List.fold_right *)
let map f l =
  List.fold_right (fun x acc -> f x :: acc) l []


(* dedup  using List.fold_right *)
let dedup l =
  List.fold_right (fun x acc ->
    match acc with
    | [] -> [x]
    | hd :: _ -> if x = hd then acc else x :: acc
  ) l []


(* filteri from basics - predicate takes index and element *)
let filteri f l =
  let rec aux i = function
    | [] -> []
    | x :: xs ->
      if f i x then x :: aux (i + 1) xs
      else aux (i + 1) xs
  in
  aux 0 l


(* filter using filteri *)
let filter f l = filteri (fun _ x -> f x) l


(* every using filteri, returns every nth element *)
let every n l = filteri (fun i _ -> (i + 1) mod n = 0) l


(* fold_while which stops early if function returns None, continues with Some v *)
let rec fold_while f acc l =
  match l with
  | [] -> acc
  | x :: xs ->
    match f acc x with
    | None -> acc
    | Some new_acc -> fold_while f new_acc xs


(* fold_left using fold_while *)
let fold_left f acc l =
  fold_while (fun acc x -> Some (f acc x)) acc l


(* sums integers while total < n, returns (count, sum) pair *)
let sum_while_less_than n l =
  fold_while (fun (count, sum) x ->
    if sum + x < n then Some (count + 1, sum + x)
    else None
  ) (0, 0) l


(* I do not enjoy working with this language. *)
