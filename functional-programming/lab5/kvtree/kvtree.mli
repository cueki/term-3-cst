module type Comparable = sig
  type t
  val compare : t -> t -> int
end

module Make (C : Comparable) : sig
  type 'v kvtree

  exception Not_found

  val empty : 'v kvtree
  val is_empty : 'v kvtree -> bool
  val find_opt : C.t -> 'v kvtree -> 'v option
  val insert : C.t -> 'v -> 'v kvtree -> 'v kvtree
  val delete : C.t -> 'v kvtree -> 'v kvtree
  val of_list : (C.t * 'v) list -> 'v kvtree
  val size : 'v kvtree -> int
  val find : C.t -> 'v kvtree -> 'v
  val to_list : 'v kvtree -> (C.t * 'v) list
  val to_string : (C.t * 'v -> string) -> 'v kvtree -> string
end
