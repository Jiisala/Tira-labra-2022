from services.logic import logic

class UI:

    def __init__(self) -> None:
        pass
    
    def start(self):
        
        logo =(">v<                                            ",
        "_+_____________________________________________\ "     ,     
        " | *      *               *    *      *** **  *|\ ",
        " |  *  *    **      *           *        *   * | \ ",
        " |   *       JAAKKO's       * *    *        *  |  \ ",
        " |     **          DUNGEON  *   ** *   *** *   +-=-> ",
        " |   *      GENERATOR  *      *    *   *  *    |  / ",
        "\| * *     *                *       * * *      | / ",
        " L__________________________________be amazed _|/  ",
        "  \                                            /  ",
        "              Lets go go go!                   ",
        "                                              ",
        "    ___[C]reate_____[S]ettings_____[Q]uit___  ")
        for row in logo:
            print (row)
        
        print()
        while True:
            next = input(">").lower()
            if next == "q":
                break
            if next == "c":
                logic.create_map()

ui = UI()
