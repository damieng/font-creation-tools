
# FontLab 5 menu commands
# Reverse engineered from FontLab 5.2.2 for Windows by DamienG

class MainMenuCommands:
    # File
    FileNew                     = 57600            
    FileOpen                    = 57601       
    FileOpenInstalled           = 34026
    FileSearch                  = 33928     
    FileClose                   = 57602            
    FileCloseAll                = 33243          
    FileSave                    = 57603            
    FileSaveAs                  = 57604            
    FileSaveAll                 = 33003            
    FileRevert                  = 33233            
    FileGenerateFont            = 33531       
    FileGenerateAll             = 33952  
    FileImportBackground        = 33040
    FileImportBitmapFont        = 33911
    FileImportEPS               = 32880
    FileImportMetrics           = 33100
    FileImportMacFontFile       = 33941
    FileFontinfo                = 33001            
    FilePrint                   = 57607            
    FileExit                    = 32865            
            
    # Edit
    EditUndo                    = 32853            
    EditRedo                    = 32854            
    EditCut                     = 57635            
    EditCopy                    = 57634            
    EditPaste                   = 57637         
    EditPasteSpecial            = 57639   
    EditInsert                  = 33183            
    EditDelete                  = 32871            
    EditDuplicate               = 32872            
    EditSelectAll               = 32873            
    EditDeselect                = 32895            
    EditInvertSelection         = 32875            
    EditFind                    = 57636         
    EditFindOutline             = 33947   
    EditAppend                  = 33391            
    EditCopyGlyph               = 32876            
    EditProperties              = 32887            
 
    # View
    ViewRulers                  = 33335            
    
    # View > Show Layers
    ShowGrid                    = 32855            
    ShowGuidelines              = 32856            
    ShowHints                   = 32857            
    ShowMask                    = 32972            
    ShowBackground              = 32858
    ShowAlignmentZones          = 32807
    ShowGlyphMetrics            = 33612            
    ShowVerticalMetrics         = 33398            
    ShowGlobalMask              = 33400      
    ShowAnchorsAndCarets        = 33401            
    ShowNodes                   = 32859            
    ShowControlVectors          = 32860            
    ShowConnections             = 32861            
    ShowNodePositions           = 33343
    ShowShapeGroup              = 33803
    ShowNeighbors               = 33813
    ShowFontAudit               = 32939            
    ShowFillOutline             = 32862            
    ShowEditMask                = 33181           

    # View > Lock Layers
    LockOutline                 = 33402            
    LockGuidelines              = 33403            
    LockHints                   = 33404            
    LockMask                    = 33405            
    LockVerticalMetrics         = 33409            
    LockGlobalMask              = 33407            
    LockGlyphMetrics            = 33408            
    LockComponents              = 33410            
    LockAnchorsAndCarets        = 33411            
    LockAlignmentZones          = 33406            
        
    # View > Snap to Layers
    SnapOutline                 = 33414            
    SnapGuidelines              = 33415            
    SnapHints                   = 33416            
    SnapMask                    = 33417            
    SnapGrid                    = 33413            
    SnapVerticalMetrics         = 33418            
    SnapGlobalMask              = 33419            
    SnapGlyphMetrics            = 33420            
    SnapAnchors                 = 33551            
    SnapAlignmentZones          = 33421            

    # View > Toolbars
    ToolbarStatusBar            = 33719
    ToolbarStandard             = 35009
    ToolbarPanels               = 30008
    ToolbarTools                = 33758
    ToolbarPaint                = 35014
    ToolbarContour              = 33761
    ToolbarMetricsTools         = 33730
    ToolbarMetricsCommands      = 33809
    ToolbarMacro                = 33220
    ToolbarUser1                = 32771
    ToolbarUser2                = 32772
    ToolbarUser3                = 32773
    ToolbarUser4                = 32774
    ToolbarUser5                = 32775
    ToolbarUser6                = 32776
    ToolbarUser7                = 32777
    ToolbarUser8                = 32778
    ToolbarUser9                = 32779
    ToolbarUser10               = 32780
    ToolbarUser11               = 32781
    ToolbarAutoHide             = 33177
    ToolbarCustomize            = 33344

    # View > Zoom
    ViewZoomCustom              = 33064            
    ViewZoomFit                 = 33065            
    ViewZoom25                  = 33066            
    ViewZoom50                  = 33067            
    ViewZoom75                  = 33068            
    ViewZoom100                 = 33069            
    ViewZoom150                 = 33071            
    ViewZoom200                 = 33072            
    ViewZoom400                 = 33726            
    ViewZoom1to4px              = 33652
    ViewZoom1to2px              = 33653
    ViewZoom1to1px              = 33654
    ViewZoom2to1px              = 33655
    ViewZoom4to1px              = 33656
    ViewZoomIn                  = 33074
    ViewZoomOut                 = 33075

    # Contour
    ContourSketchMode           = 33291
    ContourMoveNode             = 33048
    ContourInterpolateNodes     = 32918
    ContourCorrectConnections   = 32910
    ContourJoinBrokenContours   = 33644 
    ContourCloseOpenContours    = 33927
    ContourNodesAtExtremes      = 32874
    ContourOptimize             = 32911
    ContourAlignToGuides        = 32890

    # Contour > Transform
    TransformFreeTransform      = 32830
    TransformEnvelope           = 32994
    TransformFlipHorizontal     = 32908
    TransformFlipVertical       = 32909
    TransformMergeContours      = 32846
    TransformGetIntersection    = 33428
    TransformDeleteIntersection = 33507

    # Contour > Paths
    PathSetPSDirection          = 33725
    PathSetTTDirection          = 33724
    PathReverse                 = 32817
    PathReverseAll              = 32926
    PathSetStartpoints          = 32818
    PathSimplify                = 33046
    PathExpand                  = 33622
    PathMakeParallel            = 33629
    PathChangeWeight            = 34058
    PathCleanUp                 = 34054
    PathRelocateStartpoints     = 34063
    
    # Contour > Convert
    ConvertCurvesToPostScript   = 32892
    ConvertCurvesToTrueType     = 32891
    ConvertSelectionToComponent = 33646

    # Contour > Interpolate
    InterpolateHorizontal       = 34083
    InterpolateVertical         = 34084
    InterpolateRemove           = 34085

    # Glyph
    GlyphCreate                 = 32844
    GlyphCreateIfEmpty          = 33768
    GlyphAddComponent           = 33033
    GlyphEditComposite          = 33169
    GlyphDecompose              = 32925
    GlyphRename                 = 32930
    GlyphGenerate               = 33212
    
    # Glyph > Glyph Names
    GlyphNamesReencodeGlyphs    = 32929
    GlyphNamesGenerateUnicode   = 32931
    GlyphNamesClearUnicode      = 32932
    GlyphNamesGenerateNames     = 33053
    GlyphNamesSaveEncoding      = 33176

    # Glyph > Sort Glyphs
    SortGlyphsByName            = 33238
    SortGlyphsByUnicode         = 33239
    SortGlyphsByEncoding        = 33240

    # Tools
    ToolKerningAssistance       = 33607
    ToolMetricsAssistance       = 33589
    ToolAction                  = 32978
    ToolRepeatAction            = 33647
    ToolActionSet               = 32976
    ToolMergeFonts              = 33672
    ToolBlendFonts              = 33610
    ToolCustomize               = 33344
    ToolsOptions                = 32894

    # Tools > Hints & Guides
    HintsRemoveHintsBoth            = 32815
    HintsRemoveHintsHorizontal      = 32896
    HintsRemoveHintsVertical        = 32897
    HintsRemoveGuidelinesBoth       = 32898
    HintsRemoveGuidelinesHorizontal = 32899
    HintsRemoveGuidelinesVertical   = 32900
    HintsAutohinting                = 32816
    HintsAutoreplacing              = 33079
    HintsConvertHintsToLinks        = 32960
    HintsConvertLinksToHints        = 32961
    HintsAddNewHorizontalLink       = 32962
    HintsAddNewVerticalLink         = 32963
    HintsType1Hinting               = 32822
    HintsTrueTypeHinting            = 32831

    # Tools > Background
    BackgroundCreate            = 32988
    BackgroundCopy              = 33045
    BackgroundRemove            = 32989
    BackgroundMoveAndScale      = 32987
    BackgroundTracePixels       = 33925
    BackgroundTrace             = 33042

    # Tools > Mask
    MaskCopyOutlineToMask       = 32904
    MaskPasteMaskToOutline      = 32906
    MaskClear                   = 32907
    MaskSwapOutlineWithMask     = 33617
    MaskAssignFontMask          = 32973
    MaskCopyOutlineToGlobalMask = 33182
    MaskCopyMaskToGlobalMask    = 33187
    MaskPasteGlobalMaskToMask   = 33188
    MaskClearGlobalMask         = 33186

    # Tools > Multiple Master
    MasterRemoveAxis            = 32966
    MasterDefineNewAxis         = 32967
    MasterEditAxisGraph         = 32969
    MasterModifyAxisNames       = 32970
    MasterRearrange             = 33912
    MasterGenerateInstance      = 33279
    MasterExpand                = 33624
    MasterAssign                = 33641
    MasterMaskToMaster          = 33146
    MasterMatch                 = 33917

    # Tools > Quick Test As
    QuickTestAsOpenTypeTT       = 34019
    QuickTestAsOpenTypePS       = 34022

    # Tools > External Tools
    ExternalToolsTools          = 33345

    # Window
    WindowNewGlyph              = 32990            
    WindowNewMetrics            = 32991    
    WindowCascade               = 57650            
    WindowTileHorz              = 57651            
    WindowTileVert              = 57652            
    WindowCloseAll              = 33243 

    # Window > Panels
    PanelEditingLayers          = 33242      
    PanelTransformation         = 33639
    PanelEditMacro              = 33221      
    PanelOpenType               = 33202
    PanelOutput                 = 163              
    PanelPreview                = 33263
    PanelClasses                = 33272
    PanelFonts                  = 32946
    PanelFontMap                = 33376 
    PanelSmartShapes            = 32977
    PanelAxis                   = 32955            
    PanelMasters                = 32945                     

    # Window > Workspace
    WorkspaceExport             = 33977    

    # Help
    HelpKeyboardShortcuts       = 33348            
    HelpAbout                   = 33043            
    HelpAboutFontLabOnTheWeb    = 33638            

class NodeMenuCommands:
    Cancel                      = 40500
    MakeFirst                   = 40158
    ConvertPSTT                 = 40153
    Delete                      = 40150
    Duplicate                   = 40190
    RetractBCPs                 = 40194
    AddAnchor                   = 40176
    ReverseContour              = 40162
    ContourClose                = 40177
    ContourDelete               = 40161
    ContourSubtract             = 40163
    ContourSelect               = 40148
    ContourMakeParallelPath     = 40147
    ContourBreak                = 40156
    MakeCorner                  = 40191
    FixedBCPDirection           = 40142
    InterpolateHorizontal       = 40145
    InterpolateVertical         = 40146
    InterpolateRemove           = 40187
    ConnectionSmooth            = 40141
    ConnectionSharp             = 40140
    Properties                  = 40151

class FontWindowMenuCommands:
    Names                       = 33690
    UnicodeRanges               = 33691
    Codepages                   = 33692
    GlyphIndex                  = 33693

class FontToolbarCommands:
    FontInfo                    = 33001    
    Names                       = 33208
    UnicodeRanges               = 32974
    Codepages                   = 33060
    GlyphIndex                  = 33209
    SaveEncoding                = 33176

class CurveMenuCommands:
    Cancel                      = 40500
    InsertNode                  = 40152
    ConvertToVector             = 40153
    Normalize                   = 40154

class SelectionMenuCommands:
    Cancel                      = 40500
    Cut                         = 32835
    Copy                        = 32836
    Delete                      = 32812
    FreeTransform               = 32830
    RetractBCPs                 = 40194
    AlignPoints                 = 40193
    ReverseContours             = 40162
    ConvertToCurves             = 40168
    ConvertToLines              = 40171
    ConvertToOffCurve           = 40173
    InterpolateHorizontal       = 40145
    InterpolateVertical         = 40146
    InterpolateRemove           = 40187
    ConnectionSmooth            = 40141
    ConnectionSharp             = 40140
    Properties                  = 40151

class GuideMenuCommands:
    Cancel                      = 40500
    ConvertToGlobal             = 40172
    Align                       = 40169
    Delete                      = 40150
    CreateOrthogonal            = 40155
    Properties                  = 40151

class HintMenuCommands:
    Cancel                      = 40500
    ConvertToLink               = 40159
    Reverse                     = 40165
    Delete                      = 40150
    DefineAStem                 = 40186
    Properties                  = 40151

class MetricMenuCommands:
    Cancel                      = 40500
    Properties                  = 40151

class LinkMenuCommands:
    Cancel                      = 40500
    ConvertToHint               = 40164
    Reverse                     = 40166
    Delete                      = 40150
    Properties                  = 40151

class GlobalGuideMenuCommands:
    Cancel                      = 40500
    CreateLocal                 = 40178
    Align                       = 40169
    Delete                      = 40150
    IsAscender                  = 40180
    IsDescender                 = 40181
    IsCapsHeight                = 40182
    IsxHeight                   = 40183
    IsVisualAscender            = 40184
    IsVisualDescender           = 40185
    Properties                  = 40151

class AnchorMenuCommands:
    Cancel                      = 40500
    Rename                      = 40174
    Delete                      = 40150
    MarkRed                     = 40601
    MarkBlue                    = 40603
    MarkGreen                   = 40602
    MarkMagenta                 = 40604
    MarkCyan                    = 40605
    Properties                  = 40151

class ComponentMenuCommands:
    Cancel                      = 40500
    Decompose                   = 40110
    Delete                      = 40111
    CopyMetrics                 = 40199
    CopyAnchors                 = 40195
    Center                      = 40116
    Edit                        = 40197
    Properties                  = 40399

class NeighbourMenuCommands:
    Cancel                      = 40500
    EditGlyph                   = 40117
    Choose                      = 40118
 
class PreviewMenuCommands:
    TextMode                    = 33715
    MetricsMode                 = 32948
    KerningMode                 = 32949
    GenerateKernFeature         = 33934

class PreviewOptionsCommands:
    Underline                   = 33720
    Strikethrough               = 33959
    Panel                       = 33526
    Table                       = 33666
    Ruler                       = 33721
    AutomaticLineFeed           = 34075
    FlipGlyphs                  = 33804
    MeasurementLine             = 33554
    ClassKerning                = 34039
    ClassKerningWithExceptions  = 34040
    ClassKerningInKeyPairsOnly  = 34041
    IndividualPairKerning       = 34043

class MorphMenuCommands:
    OriginalPosition            = 33743
    SetDestination              = 33746
    RepeatLastLink              = 33745
    RemoveLink                  = 33744

class BitmapToolMenuCommands:
    Cancel                      = 40500
    FitToGlyph                  = 40113
    Delete                      = 40114

class TrueTypeHintingMenuCommands:
    Cancel                      = 40500
    ResetProgram                = 40201
    RemoveHCommands             = 40205
    RemoveVCommands             = 40206
    RemoveFinalDeltas           = 40202
    RemoveAllDeltas             = 40203
    ConvertHintsToInstructions  = 40204
    ReassignZones               = 40214
    ReassignStems               = 40208
    AutohintingOptions          = 40207
    PointSetMiddleDeltaMinus8   = 40221
    PointSetMiddleDeltaMinus7   = 40222
    PointSetMiddleDeltaMinus6   = 40223
    PointSetMiddleDeltaMinus5   = 40224
    PointSetMiddleDeltaMinus4   = 40225
    PointSetMiddleDeltaMinus3   = 40226
    PointSetMiddleDeltaMinus2   = 40227
    PointSetMiddleDeltaMinus1   = 40228
    PointSetMiddleDeltaPlus1    = 40229
    PointSetMiddleDeltaPlus2    = 40230
    PointSetMiddleDeltaPlus3    = 40231
    PointSetMiddleDeltaPlus4    = 40232
    PointSetMiddleDeltaPlus5    = 40233
    PointSetMiddleDeltaPlus6    = 40234
    PointSetMiddleDeltaPlus7    = 40235
    PointSetMiddleDeltaPlus8    = 40236
    PointSetFinalDeltaMinus8    = 40241
    PointSetFinalDeltaMinus7    = 40242
    PointSetFinalDeltaMinus6    = 40243
    PointSetFinalDeltaMinus5    = 40244
    PointSetFinalDeltaMinus4    = 40245
    PointSetFinalDeltaMinus3    = 40246
    PointSetFinalDeltaMinus2    = 40247
    PointSetFinalDeltaMinus1    = 40248
    PointSetFinalDeltaPlus1     = 40249
    PointSetFinalDeltaPlus2     = 40250
    PointSetFinalDeltaPlus3     = 40251
    PointSetFinalDeltaPlus4     = 40252
    PointSetFinalDeltaPlus5     = 40254
    PointSetFinalDeltaPlus6     = 40256
    PointSetFinalDeltaPlus7     = 40257
    PointSetFinalDeltaPlus8     = 40258
    PointAlignClosestPixelEdge  = 40341
    PointAlignLeftBottomEdge    = 40342
    PointAlignRightTopEdge      = 40343
    PointAlignCenterOfPixel     = 40344
    PointAlignDoubleGrid        = 40345
    SingleLinkDeleteCommand     = 40209
    SingleLinkRoundDistance     = 40211
    SingleLinkDoNotLinkToStem   = 40698
    SingleLinkAutoSelectStem    = 40210
    SingleLinkAlignToGrid       = 40212
    SingleLinkAlignClosestPixelEdge = 40341
    SingleLinkAlignLeftBottomEdge = 40342
    SingleLinkAlignRightTopEdge = 40343
    SingleLinkAlignCenterOfPixel = 40344
    SingleLinkAlignDoubleGrid   = 40345
    DoubleLinkDeleteCommand     = 40209
    DoubleLinkDoNotLinkToStem   = 40698
    DoubleLinkAutoSelectStem    = 40210
    DoubleLinkConvertSingleLeftBottom = 40396
    DoubleLinkConvertSingleRightTop = 40395
    CommandDelete               = 40209
    ZoneDeleteDelta             = 40215
    ZoneDeleteAllDeltaCommands  = 40213
    ZoneDeltaMinus8             = 40221
    ZoneDeltaMinus7             = 40222
    ZoneDeltaMinus6             = 40223
    ZoneDeltaMinus5             = 40224
    ZoneDeltaMinus4             = 40225
    ZoneDeltaMinus3             = 40226
    ZoneDeltaMinus2             = 40227
    ZoneDeltaMinus1             = 40228
    ZoneDeltaPlus1              = 40229
    ZoneDeltaPlus2              = 40230
    ZoneDeltaPlus3              = 40231
    ZoneDeltaPlus4              = 40232
    ZoneDeltaPlus5              = 40233
    ZoneDeltaPlus6              = 40234
    ZoneDeltaPlus7              = 40235
    ZoneDeltaPlus8              = 40236
    AlignDeleteCommand          = 40209
    AlignAttachToZone           = 40220
    AlignToGrid                 = 40212
    AlignClosestPixelEdge       = 40341
    AlignLeftBottomEdge         = 40342
    AlignRightTopEdge           = 40343
    AlignCenterOfPixel          = 40344
    AlignDoubleGrid             = 40345
    InterpolateDeleteCommand    = 40209
    InterpolateAlignToGrid       = 40212
    InterpolateAlignClosestPixelEdge = 40341
    InterpolateAlignLeftBottomEdge = 40342
    InterpolateAlignRightTopEdge = 40343
    InterpolateAlignCenterOfPixel = 40344
    InterpolateAlignDoubleGrid   = 40345
    DeltaDeleteCommand          = 40209
    DeltaMinus8                 = 40221
    DeltaMinus7                 = 40222
    DeltaMinus6                 = 40223
    DeltaMinus5                 = 40224
    DeltaMinus4                 = 40225
    DeltaMinus3                 = 40226
    DeltaMinus2                 = 40227
    DeltaMinus1                 = 40228
    DeltaPlus1                  = 40229
    DeltaPlus2                  = 40230
    DeltaPlus3                  = 40231
    DeltaPlus4                  = 40232
    DeltaPlus5                  = 40233
    DeltaPlus6                  = 40234
    DeltaPlus7                  = 40235
    DeltaPlus8                  = 40236
    DeltaRemoveForCurrentPPM    = 40398

class MeterToolMenuCommands:
    Cancel                      = 40500
    AddTwoGuidelinesAt100       = 40526
    AddTwoGuidelinesAt50        = 40527
    AddTwoGuidelinesAt200       = 40528
    AddHorizontalGuidelineAt100 = 40521
    AddHorizontalGuidelineAt50  = 40522
    AddHorizontalGuidelineAt200 = 40523
    AddVerticalGuidelineAt100   = 40524
    AddVerticalGuidelineAt50    = 40530
    AddVerticalGuidelineAt200   = 40525
    AddSlantedGuideline         = 40529
    SetRightSidebearing         = 40519
    SetLeftSidebearing          = 40518
    AddAnchor                   = 40520

class DrawingToolMenuCommands:
    Cancel                      = 40500
    NewDrawing                  = 40040
    ImportFromOutline           = 40041
    CopyToOutline               = 40044
    AddToOutline                = 40043

class GlyphsBarMenuCommands:
    ShowCaption                 = 33316
    Name                        = 33318
    Unicode                     = 33325
    Index                       = 33326
    Key                         = 34068
    Width                       = 33324
    Decimal                     = 33319
    Hex                         = 33320
    Octal                       = 33322
    ANSI                        = 33323
    ShowMarks                   = 33327
    AddNote                     = 33264
    OpenInNewWindow             = 34029
    OpenFontWindow              = 33078

class GlyphWindowMenuCommands:
    OutlineHMirror              = 32908
    OutlineVMirror              = 32909
    OutlineSetPSDirection       = 33725
    OutlineReverseAllPaths      = 32926
    OutlineCheckConnections     = 32910
    OutlineNodesAtExtremes      = 32874
    OutlineAlignToGuides        = 32890
    OutlineOptimize             = 32911
    OutlineExpandStrokes        = 33622
    OutlineMakeParallelPath     = 33629
    OutlineJoinAllContours      = 33644
    OutlineSelectionToComponent = 33646
    OutlineMergeContours        = 32846
    OutlineGetIntersection      = 33428
    OutlineDeleteIntersection   = 33507
    OutlineCurvesToPostScript   = 32892
    OutlineCurvesToTrueType     = 32891
    HintsAutohinting            = 32816
    HintsAutoreplacing          = 33079
    HintsConvertHintsToLinks    = 32960
    HintsConvertLinksToHints    = 32961
    HintsAddNewHorizontalLink   = 32962
    HintsAddNewVerticalLink     = 32963
    MaskCopyOutlineToMask       = 32904
    MaskPasteMaskToOutline      = 32906
    MaskClearGlobalMask         = 32907
    MaskClearMaskToMaster       = 33146
    MaskSwapOutlineWithMask     = 33617
    EditMask                    = 33181
    Action                      = 32978
    AddGlyphNote                = 33265
    AddCanvasNote               = 34091
    AddAnchor                   = 33532
    AddComponent                = 33033
    Decompose                   = 32925
    OpenFontWindow              = 33078
    Properties                  = 32887

class MacroEditorMenuCommands:
    NewProgram                  = 33184
    OpenProgram                 = 34188
    SaveProgram                 = 33185
    SaveProgramAs               = 33194
    ShowLineNumbers             = 34032
    ClosePanel                  = 33490

class OpenTypeMenuCommands:
    ResetFeatures               = 33222
    OpenFeatures                = 33210
    InterpretStoredBinaryLayoutTables = 33664
    CompileAndStoreTablesInBinaryForm = 34060
    CopyFeaturesFromAFont       = 33936
    ImportFontLabClasses        = 33823
    GenerateKernFeature         = 33934
    SaveFeatures                = 33211
    ClosePanel                  = 33490

class PaintStrokeMenuCommands:
    SmoothRight                 = 40131
    SmoothLeft                  = 40136
    PointRight                  = 40135
    PointLeft                   = 40137
    SimpleCurved                = 40132
    SimpleFlat                  = 40133
    Shaped                      = 40134
    Inflated                    = 40138
    Options                     = 40092

class PaintBrushWidthMenuCommands:
    RoundBrush                  = 40099
    FlatBrush                   = 40098
    Units20                     = 40095
    Units40                     = 40094
    Units80                     = 40093
    Units120                    = 40091
    Options                     = 40092

class FontWindowMenuCommands:
    Width8                      = 33058
    Width16                     = 33055
    Width24                     = 33056
    Width32                     = 33057
    Copy                        = 57634
    Paste                       = 57637
    AppendGlyphs                = 33391
    Delete                      = 32871
    Action                      = 32978
    AddNote                     = 33264
    Rename                      = 32930
    MarkNone                    = 33508
    MarkRed                     = 33509
    MarkBlue                    = 33510
    MarkGreen                   = 33511
    MarkMagenta                 = 33512
    MarkCyan                    = 33513
    MarkCustom                  = 33736
    SelectEncoding              = 33138
    SelectModifiedGlyphs        = 33904
    AddSuffixToName             = 33957
    CurrentGlyphIsDefault       = 33189
    RemoveUnicode               = 33218
    SaveEncoding                = 33176
    OpenGlyphWindow             = 32980
    Properties                  = 32887

class RulerMenuCommands:
    Rulers                      = 33335
    ZoomBar                     = 33648
    RemoveHintsBoth             = 32815
    RemoveHintsHorizontal       = 32896
    RemoveHintsVertical         = 32897
    RemoveGuidelinesBoth        = 32898
    RemoveGuidelinesHorizontal  = 32899
    RemoveGuidelinesVertical    = 32900
    AddNewHorizontalLink        = 32962
    AddNewVerticalLink          = 32963

class FontSpecialMenuCommands:
    GenerateTemplateFont        = 33123
    ExpandNamesFile             = 33124

class MetricsMenuCommands:
    PreviewMode                 = 32950
    TextMode                    = 33715
    KerningMode                 = 32949
    Auto                        = 33105
    Assistance                  = 33553
    OpenFontWindow              = 33078

class KerningMenuCommands:
    PreviewMode                 = 32950
    TextMode                    = 33715
    KerningMode                 = 32948
    Auto                        = 33105
    ResetKerning                = 33106
    EditKerning                 = 33125
    Assistance                  = 33553
    AddPairs                    = 33787
    GenerateKernFeature         = 33934
    OpenFontWindow              = 33078

class PreviewMenuCommands:
    Waterfall                   = 33429
    MMBlend                     = 34088
    GlyphGroup                  = 33826
    ShowMetrics                 = 33204
    VerticalOrientation         = 33662
    RightToLeft                 = 33363

class TrueTypeHintLayers:
    HintedOutline               = 40059
    GridLines                   = 40051
    PixelCenters                = 40052
    ResultingImage              = 40033
    PointNumbers                = 40054
    ProgramPanel                = 40050
    PreviewPanel                = 40055

class TrueTypeBitmapMenuCommands:
    GenerateBitmap              = 40240
    RemoveBitmap                = 40238
    CopyToBackground            = 40119
    ImportBitmaps               = 40237
    HighlightDifferences        = 40129