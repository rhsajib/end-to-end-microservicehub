import { useState } from "react";
import { RadioGroup } from "@headlessui/react";

const convertType = [
    { title: "Doc to Pdf", name: "docToPdf" },
    { title: "Docs to Pdf", name: "docsToPdf" },
    { title: "Text to Pdf", name: "textToPdf" },
];

export default function SelectType({ fileType }) {
    const [selected, setSelected] = useState(convertType[0]);

    return (
        <div className="w-full px-4 py-16">
            <div className="mx-auto w-full max-w-md">
                <RadioGroup value={selected} onChange={setSelected}>
                    <div className="space-y-2">
                        {convertType.map((type) => (
                            <RadioGroup.Option
                                key={type.name}
                                type={type}
                                className={({ active, checked }) =>
                                    `${
                                        active
                                            ? "ring-2 ring-white/60 ring-offset-2 ring-offset-sky-300"
                                            : ""
                                    }
                                    ${
                                        checked
                                            ? "bg-sky-900/75 text-white"
                                            : "bg-white"
                                    }
                                    h-4 relative flex cursor-pointer rounded-lg px-5 py-4 shadow-md focus:outline-none`
                                }
                            >
                                {({ active, checked }) => (
                                    <>
                                        <div className="flex w-full items-center justify-between">
                                            <div className="flex items-center">
                                                <div className="text-sm">
                                                    <RadioGroup.Label
                                                        as="p"
                                                        // fileType={type.name}
                                                        className={`font-medium  ${
                                                            checked
                                                                ? "text-white"
                                                                : "text-gray-900"
                                                        }`}
                                                    >
                                                        {type.title}
                                                    </RadioGroup.Label>
                                                </div>
                                            </div>
                                            {checked && (
                                                <div className="shrink-0 text-white">
                                                    <CheckIcon className="h-6 w-6" />
                                                </div>
                                            )}
                                        </div>
                                    </>
                                )}
                            </RadioGroup.Option>
                        ))}
                    </div>
                </RadioGroup>
            </div>
        </div>
    );
}

function CheckIcon(props) {
    return (
        <svg viewBox="0 0 24 24" fill="none" {...props}>
            <circle cx={12} cy={12} r={12} fill="#fff" opacity="0.2" />
            <path
                d="M7 13l3 3 7-7"
                stroke="#fff"
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="round"
            />
        </svg>
    );
}
