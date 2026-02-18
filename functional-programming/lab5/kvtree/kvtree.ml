(* Madison Lovett, A01292253
   Feb 17, 2026 *)

module type Comparable = sig
  type t
  val compare : t -> t -> int
end

module Make (C : Comparable) = struct
  type 'v kvtree = L | N of C.t * 'v * 'v kvtree * 'v kvtree

  exception Not_found

  let empty = L

  let is_empty t = t = L

  (* find key in tree *)
  let rec find_opt k t =
    match t with
    | L -> None
    | N (k', v, l, _) when C.compare k k' < 0 -> find_opt k l
    | N (k', _, _, r) when C.compare k k' > 0 -> find_opt k r
    | N (_, v, _, _) -> Some v

  (* add a key, value pair to a given tree *)
  let rec insert k v t =
    match t with
    | L -> N (k, v, L, L)
    | N (k', v', l, r) when C.compare k k' < 0 -> N (k', v', insert k v l, r)
    | N (k', v', l, r) when C.compare k k' > 0 -> N (k', v', l, insert k v r)
    | N (_, _, l, r) -> N (k, v, l, r)

  (* find a successor from the right subtree to replace *)
  let rec remove_min t =
   match t with
    | L -> failwith "remove_min: empty tree"
    | N (k, v, L, r) -> (k, v, r)
    | N (k, v, l, r) ->
      let (min_k, min_v, l') = remove_min l in
      (min_k, min_v, N (k, v, l', r))

  (* remove a node from a tree given its key *)
  let rec delete k t =
    match t with
    | L -> L
    | N (k', v', l, r) when C.compare k k' < 0 -> N (k', v', delete k l, r)
    | N (k', v', l, r) when C.compare k k' > 0 -> N (k', v', l, delete k r)
    | N (_, _, L, r) -> r
    | N (_, _, l, L) -> l
    | N (_, _, l, r) ->
      let (succ_k, succ_v, r') = remove_min r in
      N (succ_k, succ_v, l, r')

  (* create a tree of a list (k, v) *)
  let of_list lst =
    List.fold_left (fun acc (k, v) -> insert k v acc) L lst

  (* return a counter that adds one for every node in tree *)
  let rec size t =
    match t with
    | L -> 0
    | N (_, _, l, r) -> 1 + size l + size r

  (* return value from key or raise Not_found *)
  let rec find k t =
    match t with
    | L -> raise Not_found
    | N (k', v, l, _) when C.compare k k' < 0 -> find k l
    | N (k', _, _, r) when C.compare k k' > 0 -> find k r
    | N (_, v, _, _) -> v

  (* return a kvtree converted a to list in ascending order *)
  let rec to_list t =
    match t with
    | L -> []
    | N (k, v, l, r) -> to_list l @ [(k, v)] @ to_list r

  (* return a kvtree converted to nested string representation *)
  let rec to_string f t =
    match t with
    | L -> "#"
    | N (k, v, l, r) ->
      "^(" ^ f (k, v) ^ ", " ^
      to_string f l ^ ", " ^
      to_string f r ^ ")"

end
